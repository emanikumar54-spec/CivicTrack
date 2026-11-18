
from style import apply_custom_style
from auth import require_admin, logout
if not require_admin():
    st.stop()
import streamlit as st
import pandas as pd

from database import (
    initialize_database,
    get_all_complaints,
    update_complaint_status,
    delete_complaint
)

initialize_database()

st.set_page_config(
    page_title="Admin Dashboard | CivicTrack",
    page_icon="⚙️",
    layout="wide"
)
apply_custom_style()
st.title("⚙️ Admin Dashboard")
st.write("Manage and monitor public infrastructure complaints.")

st.divider()
if st.button("Logout"):
    logout()

complaints = get_all_complaints()

if not complaints:
    st.info("No complaints available. Submit a complaint first.")
    st.stop()

df = pd.DataFrame(complaints)

# Dashboard metrics
st.subheader("System Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Complaints", len(df))
col2.metric("Pending", len(df[df["status"] == "Pending"]))
col3.metric("In Progress", len(df[df["status"] == "In Progress"]))
col4.metric("Resolved", len(df[df["status"] == "Resolved"]))

st.divider()

# Filters
st.subheader("🔍 Search and Filter Complaints")

col1, col2, col3 = st.columns(3)

with col1:
    priority_filter = st.selectbox(
        "Filter by Priority",
        ["All", "Critical", "High", "Medium", "Low"]
    )

with col2:
    status_filter = st.selectbox(
        "Filter by Status",
        ["All", "Pending", "In Progress", "Resolved"]
    )

with col3:
    category_filter = st.selectbox(
        "Filter by Category",
        ["All"] + sorted(df["category"].unique().tolist())
    )

search = st.text_input(
    "Search Complaint ID or Location"
)

filtered = df.copy()

if priority_filter != "All":
    filtered = filtered[
        filtered["priority"] == priority_filter
    ]

if status_filter != "All":
    filtered = filtered[
        filtered["status"] == status_filter
    ]

if category_filter != "All":
    filtered = filtered[
        filtered["category"] == category_filter
    ]

if search.strip():
    filtered = filtered[
        filtered["complaint_id"].str.contains(
            search, case=False, na=False
        )
        |
        filtered["location"].str.contains(
            search, case=False, na=False
        )
    ]

st.write(f"Showing {len(filtered)} complaints")

display_columns = [
    "complaint_id",
    "name",
    "category",
    "location",
    "priority",
    "priority_score",
    "status",
    "created_at"
]

st.dataframe(
    filtered[display_columns],
    use_container_width=True,
    hide_index=True
)

st.divider()

# Complaint details
st.subheader("📋 Complaint Details")

selected_id = st.selectbox(
    "Select Complaint",
    df["complaint_id"].tolist()
)

selected = df[
    df["complaint_id"] == selected_id
].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.write("**Complaint ID:**", selected["complaint_id"])
    st.write("**Name:**", selected["name"])
    st.write("**Phone:**", selected["phone"])
    st.write("**Category:**", selected["category"])
    st.write("**Location:**", selected["location"])

with col2:
    st.write("**Priority:**", selected["priority"])
    st.write("**Priority Score:**", selected["priority_score"])
    st.write("**Severity:**", selected["severity"])
    st.write("**People Affected:**", selected["people_affected"])
    st.write("**Safety Impact:**", selected["safety_impact"])

st.write("**Description:**")
st.info(selected["description"])

st.write("**Submitted:**", selected["created_at"])

st.divider()

# Update status
st.subheader("🔄 Update Complaint Status")

current_status = selected["status"]

new_status = st.selectbox(
    "Choose New Status",
    ["Pending", "In Progress", "Resolved"],
    index=["Pending", "In Progress", "Resolved"].index(
        current_status
    )
)

if st.button("Update Status", use_container_width=True):

    if update_complaint_status(selected_id, new_status):
        st.success("Complaint status updated successfully!")
        st.rerun()
    else:
        st.error("Unable to update complaint.")

st.divider()

# Delete complaint
st.subheader("🗑️ Delete Complaint")

confirm_delete = st.checkbox(
    "I confirm that I want to permanently delete this complaint."
)

if st.button(
    "Delete Selected Complaint",
    disabled=not confirm_delete
):
    if delete_complaint(selected_id):
        st.success("Complaint deleted successfully!")
        st.rerun()
    else:
        st.error("Unable to delete complaint.")

st.caption(
    "CivicTrack | Administrator Management Panel"
)
