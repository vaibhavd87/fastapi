import streamlit as st

def show_login_page():
    st.title('Login')

    # Hardcoded user credentials (for demonstration; not secure)
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        # This is a simple check. Replace with a secure validation in production
        if username == 'admin' and password == 'password':
            # Set the session state to indicate the user is logged in
            st.session_state['authenticated'] = True
            st.experimental_rerun()
        else:
            st.error('Incorrect username or password.')
