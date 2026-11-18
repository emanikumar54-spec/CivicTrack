
from style import apply_custom_style
import streamlit as st
from database import initialize_database, get_complaint

initialize_database()

st.set_page_config(
    page_title="Track Complaint | CivicTrack",
    page_icon="📍",
    layout="wide"
)
apply_custom_style()
st.title("📍 Track Your Complaint")

st.write(
    "Enter your complaint ID to check the latest status "
    "of your infrastructure complaint."
)

st.divider()

complaint_id = st.text_input(
    "Complaint ID",
    placeholder="Example: CIVIC-20261118-0001"
)

if st.button("Track Complaint", use_container_width=True):

    if not complaint_id.strip():
        st.warning("Please enter your complaint ID.")

    else:
        complaint = get_complaint(
            complaint_id.strip().upper()
        )

        if complaint:

            st.success("Complaint found successfully!")

            st.subheader("Complaint Information")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Complaint ID:**", complaint["complaint_id"])
                st.write("**Name:**", complaint["name"])
                st.write("**Category:**", complaint["category"])
                st.write("**Location:**", complaint["location"])

            with col2:
                st.write("**Priority:**", complaint["priority"])
                st.write("**Priority Score:**", complaint["priority_score"])
                st.write("**Submitted:**", complaint["created_at"])

            st.write("**Problem Description:**")
            st.info(complaint["description"])

            st.divider()

            st.subheader("Current Complaint Status")

            status = complaint["status"]

            if status == "Pending":
                st.warning("⏳ Your complaint is Pending.")

            elif status == "In Progress":
                st.info("🔧 Your complaint is being addressed.")

            elif status == "Resolved":
                st.success("✅ Your complaint has been resolved.")

            progress_values = {
                "Pending": 0.25,
                "In Progress": 0.65,
                "Resolved": 1.0
            }

            st.progress(progress_values[status])

            st.write("**Status:**", status)

            st.write(
                "**Last Updated:**",
                complaint["updated_at"]
            )

        else:
            st.error(
                "Complaint not found. Please check your Complaint ID."
            )

st.divider()

st.caption("CivicTrack | Complaint Tracking Portal")
