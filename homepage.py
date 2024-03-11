import streamlit as st

def show_homepage():
    """Display the homepage content."""
    st.title('Homepage')
    st.write('Welcome to the homepage!')
    if st.button('Logout'):
        if 'user' in st.session_state:
            del st.session_state['user']
        st.write('You have been logged out.')
