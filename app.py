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


# Simulating a content database
content_db = []

def add_content(title, category, content):
    content_db.append({'title': title, 'category': category, 'content': content})

def get_content_by_category(category):
    return [content for content in content_db if content['category'] == category]

st.title('Marriage Awareness Website')

menu = ['Home', 'Login', 'SignUp', 'Add Content', 'View Content']
choice = st.sidebar.selectbox('Menu', menu)

# User management sections...

if choice == 'Add Content':
    st.subheader('Add Educational Content')
    
    with st.form(key='content_form'):
        title = st.text_input('Title')
        category = st.selectbox('Category', ['Legal', 'Responsibilities', 'General'])
        content = st.text_area('Content')
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            add_content(title, category, content)
            st.success('Content added successfully!')

elif choice == 'View Content':
    st.subheader('Educational Content')
    selected_category = st.selectbox('Select a Category to Filter', ['All', 'Legal', 'Responsibilities', 'General'])
    
    if selected_category == 'All':
        for content in content_db:
            st.write(f"### {content['title']}")
            st.write(f"**Category**: {content['category']}")
            st.write(content['content'])
    else:
        filtered_contents = get_content_by_category(selected_category)
        for content in filtered_contents:
            st.write(f"### {content['title']}")
            st.write(f"**Category**: {content['category']}")
            st.write(content['content'])
