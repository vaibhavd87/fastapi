import streamlit as st
import pandas as pd

# Simulating a database with a global variable
# WARNING: This is not recommended for production use
users_db = []

def register_user(username, password):
    users_db.append({'username': username, 'password': password})

def check_user(username, password):
    for user in users_db:
        if user['username'] == username and user['password'] == password:
            return True
    return False

st.title('User Management Service')

menu = ['Home', 'Login', 'SignUp']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.subheader('Home')

elif choice == 'Login':
    st.subheader('Login Section')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    
    if st.button('Login'):
        if check_user(username, password):
            st.success(f'Logged In as {username}')
        else:
            st.warning('Incorrect Username/Password')

elif choice == 'SignUp':
    st.subheader('Create New Account')
    new_username = st.text_input('Username', key='new_user')
    new_password = st.text_input('Password', type='password', key='new_pass')
    
    if st.button('SignUp'):
        register_user(new_username, new_password)
        st.success(f'Account created for {new_username}')
