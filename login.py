import streamlit as st
from db import login_user
from signup import show_signup_page

def show_login_page():
    st.title("Login")

    username = st.text_input("Username", key="login_username")  # Unique key
    password = st.text_input("Password", type='password', key="login_password")  # Unique key

    if st.button("Login"):
        if login_user(username, password):
            st.success(f"Logged In as {username}")
            st.session_state['logged_in'] = True
        else:
            st.error("Incorrect Username/Password")

    if st.button("Sign up"):
        show_signup_page()
