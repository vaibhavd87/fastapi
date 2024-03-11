import streamlit as st
from db import create_connection, get_user

def login_user():
    """Login form for the application."""
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        conn = create_connection('app.db')
        user = get_user(conn, username)
        if user and user[0][2] == password:
            st.session_state['user'] = username
            st.success('Logged in successfully!')
            return True
        else:
            st.error('Invalid username or password')
            return False
