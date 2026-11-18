
import streamlit as st

st.set_page_config(
    page_title="CivicTrack",
    page_icon="🏙️",
    layout="wide"
)

from style import apply_custom_style
from database import initialize_database, get_all_complaints

apply_custom_style()
initialize_database()

st.title("🏙️ CivicTrack")

st.subheader(
    "Intelligent Public Infrastructure Complaint Prioritisation System"
)

st.write(
    "A smart platform for reporting, prioritising and tracking "
    "public infrastructure complaints."
)

complaints = get_all_complaints()

total = len(complaints)
pending = sum(c["status"] == "Pending" for c in complaints)
progress = sum(c["status"] == "In Progress" for c in complaints)
resolved = sum(c["status"] == "Resolved" for c in complaints)
critical = sum(c["priority"] == "Critical" for c in complaints)

st.divider()

st.subheader("📊 System Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Complaints", total)
col2.metric("Pending", pending)
col3.metric("In Progress", progress)
col4.metric("Resolved", resolved)
col5.metric("Critical", critical)

st.divider()

st.subheader("🚀 Welcome to CivicTrack")

col1, col2 = st.columns(2)

with col1:
    st.info(
        "📝 Submit Complaints\n\n"
        "Report damaged roads, drainage problems and "
        "other public infrastructure issues."
    )

with col2:
    st.info(
        "🔎 Track Complaints\n\n"
        "Monitor complaint status and check whether "
        "your reported issue has been resolved."
    )

st.divider()

st.subheader("🔥 Recent Complaints")

if complaints:
    for complaint in complaints[:5]:
        with st.expander(
            f'{complaint["complaint_id"]} | '
            f'{complaint["category"]} | '
            f'{complaint["priority"]}'
        ):
            st.write("Location:", complaint["location"])
            st.write("Description:", complaint["description"])
            st.write("Status:", complaint["status"])
            st.write("Priority Score:", complaint["priority_score"])
else:
    st.info("No complaints registered yet.")

st.caption("CivicTrack | Public Infrastructure Management System")
