import streamlit as st
from signup import show_signup_page
from login import show_login_page
from homepage import show_homepage
from db import create_users_table

# Initialize the users table
create_users_table()

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Main app
def main():
    if st.session_state['logged_in']:
        show_homepage()
    else:
        show_login_page()

if __name__ == '__main__':
    main()
