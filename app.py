import streamlit as st

# --- Global Streamlit Page Configuration ---
st.set_page_config(
    page_title="StrokeRisk AI System - Login",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Session State Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- Main Application Logic ---
if __name__ == "__main__":
    
    # Hardcoded credentials for demonstration
    VALID_MEDIC_ID = "medic123"
    VALID_PASSWORD = "password123"

    # Check if already logged in and redirect
    if st.session_state['logged_in']:
        st.switch_page("pages/01_Home.py")
    else:
        # Use columns to center the login form on the page
        col1, col2, col3 = st.columns([1, 0.5, 1])

        with col2:
            st.markdown(
                """
                <div class="flex flex-col items-center justify-center p-8 bg-white rounded-lg shadow-xl w-full">
                    <h1 class="text-4xl font-black mb-2 text-center text-[#3f8abf]">🏥</h1>
                    <h2 class="text-2xl font-bold mb-1 text-center text-[#121516]">Welcome Back!</h2>
                    <p class="text-gray-500 text-sm mb-6 text-center">Login to your StrokeRisk account</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Use a Streamlit form for the login inputs
            with st.form("login_form", clear_on_submit=True):
                medic_id = st.text_input("MedicID", placeholder="Enter your MedicID", key="medic_id_input")
                password = st.text_input("Password", type="password", placeholder="Enter your password", key="password_input")
                login_button = st.form_submit_button("Login", use_container_width=True)

            if login_button:
                if medic_id == VALID_MEDIC_ID and password == VALID_PASSWORD:
                    st.session_state['logged_in'] = True
                    st.success("Login successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("Invalid MedicID or Password. Please try again.")

            # Add an additional link or message
            st.markdown(
                "<p style='text-align: center; color: #6a7781; font-size: 0.875rem; margin-top: 1rem;'>Don't have access? Contact your administrator.</p>",
                unsafe_allow_html=True
            )
