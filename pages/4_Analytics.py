
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import initialize_database, get_all_complaints
from style import apply_custom_style


st.set_page_config(
    page_title="Analytics | CivicTrack",
    page_icon="📊",
    layout="wide"
)

apply_custom_style()
initialize_database()

st.title("📊 CivicTrack Analytics")
st.write(
    "Analyze public infrastructure complaints and system performance."
)

st.divider()

complaints = get_all_complaints()

if not complaints:
    st.info(
        "No complaint data available. "
        "Submit complaints to view analytics."
    )
    st.stop()

df = pd.DataFrame(complaints)

# Overall statistics
total = len(df)
pending = (df["status"] == "Pending").sum()
progress = (df["status"] == "In Progress").sum()
resolved = (df["status"] == "Resolved").sum()
critical = (df["priority"] == "Critical").sum()

resolution_rate = (resolved / total) * 100

st.subheader("Overall Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Complaints", total)
c2.metric("Critical Complaints", int(critical))
c3.metric("Resolved", int(resolved))
c4.metric("Resolution Rate", f"{resolution_rate:.1f}%")

st.divider()

# Priority distribution
st.subheader("1. Priority Distribution")

priority_counts = (
    df["priority"]
    .value_counts()
    .reindex(["Critical", "High", "Medium", "Low"], fill_value=0)
)

fig, ax = plt.subplots()
priority_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    ax=ax
)
ax.set_ylabel("")
ax.set_title("Complaints by Priority")

st.pyplot(fig)
plt.close(fig)

st.divider()

# Category analysis
st.subheader("2. Category-wise Complaint Analysis")

category_counts = df["category"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
category_counts.plot(kind="bar", ax=ax)

ax.set_title("Complaints by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Number of Complaints")
ax.tick_params(axis="x", rotation=30)

st.pyplot(fig)
plt.close(fig)

st.write(
    "Most reported category:",
    category_counts.idxmax()
)

st.divider()

# Status analysis
st.subheader("3. Complaint Status Analysis")

status_counts = (
    df["status"]
    .value_counts()
    .reindex(
        ["Pending", "In Progress", "Resolved"],
        fill_value=0
    )
)

fig, ax = plt.subplots()
status_counts.plot(kind="bar", ax=ax)

ax.set_title("Complaint Status Overview")
ax.set_xlabel("Status")
ax.set_ylabel("Number of Complaints")

st.pyplot(fig)
plt.close(fig)

st.divider()

# Priority summary
st.subheader("4. Priority Summary")

priority_summary = pd.DataFrame({
    "Priority": priority_counts.index,
    "Number of Complaints": priority_counts.values
})

st.dataframe(
    priority_summary,
    use_container_width=True,
    hide_index=True
)

st.divider()

# Complete complaint report
st.subheader("5. Complete Complaint Report")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Complete Report (CSV)",
    data=csv_data,
    file_name="civictrack_complaints_report.csv",
    mime="text/csv",
    use_container_width=True
)

st.success("Analytics dashboard generated successfully!")

st.caption(
    "CivicTrack | Analytics and Reporting System"
)
