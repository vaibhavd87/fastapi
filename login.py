import streamlit as st
from db import login_user

def show_login_page(navigate_to):
    st.title("Login")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type='password', key="login_password")

    if st.button("Login"):
        if login_user(username, password):
            st.session_state['logged_in'] = True
            navigate_to('home')
        else:
            st.error("Incorrect Username/Password")

    if st.button("Login"):
        navigate_to('login')
