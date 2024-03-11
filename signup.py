import streamlit as st
import db

def show_signup_page():
    st.title("Signup")
    new_username = st.text_input("User Name")
    new_password = st.text_input("Password", type='password')

    if st.button("Signup"):
        if db.check_user(new_username):
            st.error("Username already exists")
        else:
            db.add_userdata(new_username, new_password)
            st.success("You have successfully created an account. Go to the login page to login.")
