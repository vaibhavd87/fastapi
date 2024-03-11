import streamlit as st
from db import add_userdata

def show_signup_page():
    st.title("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')

    if st.button("Signup"):
        add_userdata(new_user, new_password)
        st.success("You have successfully created an account")
        st.info("Go to Login Menu to login")
