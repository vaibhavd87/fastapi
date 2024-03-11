import streamlit as st
from login import login_user
from home import show_homepage
from db import create_connection, create_table

# Initialize the database connection and tables
conn = create_connection('app.db')
create_table(conn)

# Main application logic
if 'user' not in st.session_state:
    # Show the login page if the user is not logged in
    logged_in = login_user()
    if logged_in:
        show_homepage()
else:
    # If the user is logged in, show the homepage
    show_homepage()
