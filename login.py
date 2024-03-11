import streamlit as st
from db import login_user

def show_login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if login_user(username, password):
            st.success("Logged In as {}".format(username))
            st.session_state['logged_in'] = True
            st.experimental_rerun()
        else:
            st.error("Incorrect Username/Password")
