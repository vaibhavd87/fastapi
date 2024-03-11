import streamlit as st
from db import add_userdata

def show_signup_page():
    st.title("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')

    if st.button("Signup"):
        add_userdata(new_user, new_password)
        st.success("You have successfully created an account")
        st.info("Please go back and log in with your new credentials.")

    if st.button("Back to Login"):
        # Here, we simulate returning to the login page.
        # In this simplistic approach, we just call `st.experimental_rerun()`
        # Assuming this resets the app to its initial state, showing the login page.
        # Note: This might not directly work as intended without managing the session state or app flow more comprehensively.
        st.experimental_rerun()
