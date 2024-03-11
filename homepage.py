import streamlit as st

def show_homepage(navigate_to=None):
    st.title("Homepage")
    # Example content
    st.write("Welcome to the homepage!")

    # Example use of navigate_to (if you decide to implement logout or other navigation)
    if navigate_to:
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            navigate_to('login')
