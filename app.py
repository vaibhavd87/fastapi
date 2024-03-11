import streamlit as st
from homepage import show_homepage
from login import show_login_page
from signup import show_signup_page
from db import create_users_table

# Initialize the users table
create_users_table()

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'login'

# Navigation function
def navigate_to(page):
    st.session_state['current_page'] = page

# Main app function to show pages based on current state
def main():
    if st.session_state['current_page'] == 'home':
        show_homepage(navigate_to)
    elif st.session_state['current_page'] == 'signup':
        show_signup_page(navigate_to)
    else:  # Default to login page
        show_login_page(navigate_to)

if __name__ == '__main__':
    main()
