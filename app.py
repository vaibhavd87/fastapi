import streamlit as st
from signup import show_signup_page
from login import show_login_page
from homepage import show_homepage
from db import create_users_table

# Initialize the users table
create_users_table()

# Main app
def main():
    st.sidebar.title("Navigation")
    menu = ["Home", "Login", "Signup"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        show_homepage()
    elif choice == "Login":
        show_login_page()
    elif choice == "Signup":
        show_signup_page()

if __name__ == '__main__':
    main()
