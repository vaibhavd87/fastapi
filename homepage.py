import streamlit as st

def show_homepage():
    st.title("Homepage")
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.experimental_rerun()
