
from style import apply_custom_style
import streamlit as st
from database import initialize_database, add_complaint
from priority_engine import calculate_priority

initialize_database()

st.set_page_config(
    page_title="Submit Complaint | CivicTrack",
    page_icon="📝",
    layout="wide"
)
apply_custom_style()
st.title("📝 Submit a Complaint")
st.write("Report public infrastructure problems in your area.")

st.divider()

with st.form("complaint_form"):

    st.subheader("Personal Information")

    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")

    st.subheader("Complaint Information")

    category = st.selectbox(
        "Complaint Category",
        [
            "Road Damage",
            "Water Supply",
            "Electricity",
            "Sanitation",
            "Street Lights",
            "Drainage",
            "Other"
        ]
    )

    location = st.text_input(
        "Complaint Location",
        placeholder="Enter area, street or landmark"
    )

    description = st.text_area(
        "Describe the Problem",
        placeholder="Explain the infrastructure problem..."
    )

    st.subheader("Impact Assessment")

    severity = st.slider(
        "Problem Severity",
        min_value=1,
        max_value=5,
        value=3,
        help="1 = Minor, 5 = Extremely severe"
    )

    people_affected = st.number_input(
        "Estimated Number of People Affected",
        min_value=1,
        max_value=100000,
        value=10
    )

    safety_impact = st.slider(
        "Public Safety Impact",
        min_value=0,
        max_value=5,
        value=2,
        help="0 = No safety impact, 5 = Very high safety impact"
    )

    submitted = st.form_submit_button(
        "🚀 Submit Complaint",
        use_container_width=True
    )

    if submitted:

        if not name.strip():
            st.error("Please enter your name.")

        elif not location.strip():
            st.error("Please enter the complaint location.")

        elif not description.strip():
            st.error("Please describe the problem.")

        elif not phone.isdigit() or len(phone) != 10:
            st.error("Please enter a valid 10-digit phone number.")

        else:
            result = calculate_priority(
                severity,
                people_affected,
                safety_impact,
                category
            )

            complaint_data = {
                "name": name.strip(),
                "phone": phone,
                "category": category,
                "location": location.strip(),
                "description": description.strip(),
                "severity": severity,
                "people_affected": people_affected,
                "safety_impact": safety_impact,
                "priority": result["priority"],
                "priority_score": result["priority_score"]
            }

            try:
                complaint_id = add_complaint(complaint_data)

                st.success("Complaint submitted successfully!")

                st.subheader("Complaint Details")

                st.write("Complaint ID:", complaint_id)
                st.write("Priority:", result["priority"])
                st.write("Priority Score:", result["priority_score"])

                st.info(
                    "Save your complaint ID to track its progress."
                )

            except Exception as e:
                st.error(f"Unable to submit complaint: {e}")

st.divider()

st.caption("CivicTrack | Smart Complaint Registration")
