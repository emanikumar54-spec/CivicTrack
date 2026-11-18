
import streamlit as st
import hmac


def require_admin():

    if st.session_state.get("authenticated", False):
        return True

    st.title("🔐 Admin Login")
    st.write("Sign in to access the CivicTrack administration panel.")

    with st.form("admin_login"):

        username = st.text_input("Admin Username")
        password = st.text_input(
            "Admin Password",
            type="password"
        )

        submitted = st.form_submit_button(
            "Login",
            use_container_width=True
        )

        if submitted:
            try:
                correct_username = st.secrets["admin"]["username"]
                correct_password = st.secrets["admin"]["password"]

                valid_username = hmac.compare_digest(
                    username,
                    correct_username
                )

                valid_password = hmac.compare_digest(
                    password,
                    correct_password
                )

                if valid_username and valid_password:
                    st.session_state["authenticated"] = True
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

            except (KeyError, FileNotFoundError):
                st.error(
                    "Admin credentials are not configured. "
                    "Create .streamlit/secrets.toml first."
                )

    return False


def logout():
    st.session_state["authenticated"] = False
    st.rerun()
