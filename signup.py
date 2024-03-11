import streamlit as st
from db import add_userdata

def show_signup_page():
    st.title("Create New Account")
    new_user = st.text_input("Username", key="signup_username")  # Unique key
    new_password = st.text_input("Password", type='password', key="signup_password")  # Unique key

    if st.button("Signup"):
        add_userdata(new_user, new_password)
        st.success("You have successfully created an account")
        st.info("Please go back and log in with your new credentials.")

    if st.button("Back to Login"):
        st.experimental_rerun()
