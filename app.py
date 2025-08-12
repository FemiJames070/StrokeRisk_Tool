# --- 1. Global Streamlit Page Configuration ---
st.set_page_config(
    page_title="StrokeRisk AI System - Login",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Global Styling Injection (Simplified) ---
def inject_global_css_and_fonts():
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin>
        <link
            rel="stylesheet"
            as="style"
            onload="this.rel='stylesheet'"
            href="https://fonts.googleapis.com/css2?display=swap&family=Noto+Sans%3Awght%40400%3B500%3B700%3B900&family=Public+Sans%3Awght%40400%3B500%3B700%3B900"
        />
        <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
        <style>
            /* A simplified CSS to center and constrain the login form */
            .main .block-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding-top: 0 !important;
            }
            .login-card {
                max-width: 600px; /* Adjust this value for the desired width */
                width: 100%;
                padding: 2rem;
                background-color: white;
                border-radius: 0.75rem; /* rounded-lg */
                box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1); /* shadow-xl */
            }
            /* You can still keep your custom styles for inputs and buttons if you like */
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Session State Initialization for Backend Logic ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- Main Application Flow (Login Page) ---
if __name__ == "__main__":
    inject_global_css_and_fonts()

    VALID_MEDIC_ID = "medic123"
    VALID_PASSWORD = "password123"

    if st.session_state['logged_in']:
        st.switch_page("pages/01_Home.py")
    else:
        # Use columns to center the form, with wider central column
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.markdown(
                """
                <div class="login-card">
                    <h1 class="text-4xl font-black mb-2 text-center text-[#3f8abf]">🏥</h1>
                    <h2 class="text-2xl font-bold mb-1 text-center text-[#121516]">Welcome Back!</h2>
                    <p class="text-gray-500 text-sm mb-6 text-center">Login to your StrokeRisk account</p>
                """,
                unsafe_allow_html=True
            )

            # Use a Streamlit form for the login inputs
            with st.form("login_form", clear_on_submit=True):
                medic_id = st.text_input("MedicID", placeholder="Enter your MedicID")
                password = st.text_input("Password", type="password", placeholder="Enter your password")
                login_button = st.form_submit_button("Login")

                if login_button:
                    if medic_id == VALID_MEDIC_ID and password == VALID_PASSWORD:
                        st.session_state['logged_in'] = True
                        st.success("Login successful! Redirecting...")
                        st.rerun()
                    else:
                        st.error("Invalid MedicID or Password. Please try again.")

            st.markdown(
                """
                    <p class="text-center text-gray-500 text-sm mt-4">Don't have access? Contact your administrator.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
