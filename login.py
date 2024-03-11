import streamlit as st
import db
from homepage import show_homepage
import signup  # Import the signup module

def show_login_page():
    st.title("Login")
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if db.login_user(username, password):
            show_homepage(username)  # Directs to the homepage if login is successful
        else:
            st.error("Incorrect username/password")

    if st.button("Signup"):
        signup.show_signup_page()  # Directs to the signup page
