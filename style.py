
import streamlit as st


def apply_custom_style():
    st.markdown("""
    <style>
    .stApp {
        background-color: #f4f7fc;
        color: #172b4d;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #f4f7fc;
    }

    [data-testid="stHeader"] {
        background-color: transparent;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    html, body, [class*="css"] {
        font-family: Arial, sans-serif;
    }

    h1, h2, h3, p, label, span {
        color: #172b4d;
    }

    section[data-testid="stSidebar"] {
        background-color: #101d35;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    div[data-testid="stMetric"] {
        background: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
    }

    div.stButton > button {
        background-color: #2457d6;
        color: white;
        border-radius: 9px;
        border: none;
        padding: 10px 20px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #163fa8;
        color: white;
    }

    div[data-testid="stForm"] {
        background: white;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 10px;
    }

    hr {
        border-color: #dce4f0;
    }
    </style>
    """, unsafe_allow_html=True)
