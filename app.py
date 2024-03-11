import streamlit as st
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, and_
from sqlalchemy.orm import sessionmaker
import os

# Database connection
DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

# Define tables
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String),
              Column('password', String)  # For demonstration; use hashed passwords in production
              )

content = Table('content', metadata,
                Column('id', Integer, primary_key=True),
                Column('title', String),
                Column('category', String),
                Column('content', String)
                )

metadata.create_all(engine)  # Create tables if they don't exist

def register_user(username, password):
    with engine.connect() as connection:
        stmt = users.insert().values(username=username, password=password)
        connection.execute(stmt)

def check_user(username, password):
    with engine.connect() as connection:
        stmt = select([users]).where(and_(users.c.username == username, users.c.password == password))
        result = connection.execute(stmt).fetchone()
        return result is not None

def add_content(title, category, content_text):
    with engine.connect() as connection:
        stmt = content.insert().values(title=title, category=category, content=content_text)
        connection.execute(stmt)

def get_content_by_category(category):
    with engine.connect() as connection:
        if category == 'All':
            stmt = select([content])
        else:
            stmt = select([content]).where(content.c.category == category)
        return connection.execute(stmt).fetchall()

# Your Streamlit UI code here, modified to use these functions for database operations


# Initialize session state for user management
if 'username' not in st.session_state:
    st.session_state['username'] = None

# User and content database simulation
users_db = []
content_db = []

# User management functions
def register_user(username, password):
    users_db.append({'username': username, 'password': password})

def check_user(username, password):
    for user in users_db:
        if user['username'] == username and user['password'] == password:
            return True
    return False

def fake_login(username):
    st.session_state['username'] = username

def logout():
    if 'username' in st.session_state:
        del st.session_state['username']

# Content management functions
def add_content(title, category, content):
    content_db.append({'title': title, 'category': category, 'content': content})

def get_content_by_category(category):
    return [content for content in content_db if content['category'] == category]

# App title and dynamic menu based on login state
st.title('Marriage Awareness Website')

menu_items = ['Home']

if st.session_state['username'] is None:
    menu_items.extend(['Login', 'SignUp'])
else:
    menu_items.extend(['Add Content', 'View Content', 'Logout'])

choice = st.sidebar.selectbox('Menu', menu_items)

# Menu actions
if choice == 'Home':
    st.subheader('Welcome to the Marriage Awareness Website')

elif choice == 'Login':
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if check_user(username, password):
            fake_login(username)  # Simplified login
            st.success(f'Logged In as {username}')
            st.experimental_rerun()
        else:
            st.error('Incorrect Username/Password')

elif choice == 'SignUp':
    new_username = st.text_input('Username', key='new_user')
    new_password = st.text_input('Password', type='password', key='new_pass')
    if st.button('SignUp'):
        register_user(new_username, new_password)
        st.success(f'Account created for {new_username}')

elif choice == 'Add Content' and st.session_state['username']:
    with st.form(key='content_form'):
        title = st.text_input('Title')
        category = st.selectbox('Category', ['Legal', 'Responsibilities', 'General'])
        content = st.text_area('Content')
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            add_content(title, category, content)
            st.success('Content added successfully!')

elif choice == 'View Content':
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

elif choice == 'Logout':
    logout()
    st.success('You have been logged out.')
    st.experimental_rerun()
