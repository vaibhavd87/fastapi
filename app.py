from login import show_login_page
import streamlit as st

# Check if the user is authenticated
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    show_login_page()
else:
    # Initialize session state to store the checklist
    if 'checklist' not in st.session_state:
        # Define default checklist items
        st.session_state.checklist = [
            {'task': 'Do not hit your partner', 'completed': False},
            {'task': 'Do not blackmail because of past', 'completed': False},
            {'task': 'Do you know the Boundaries of Family members?', 'completed': False},
            {'task': 'How many childrens you want and when?', 'completed': False},
            {'task': 'Do not touch during menstrual cycles.', 'completed': False},
            {'task': 'Give 10% of your salary to partner and mother in case they are dependent (and do not ask where they are spending)', 'completed': False}
        ]

    # Title of the app
    st.title('Relationship Checklist')

    # Text input for new task
    new_task = st.text_input('Enter a task:', '')

    # Button to add new task
    if st.button('Add Task'):
        if new_task:  # Ensure the task is not empty
            st.session_state.checklist.append({'task': new_task, 'completed': False})
        else:
            st.warning('Please enter a task.')

    # Display checklist
    for i, task_info in enumerate(st.session_state.checklist[:]):
        col1, col2, col3 = st.columns([0.05, 0.8, 0.15])
        with col1:
            # Checkbox to mark task as completed, with a unique key
            completed = st.checkbox("", key=f"chkbox-{i}", value=task_info['completed'])
            if completed:
                st.session_state.checklist[i]['completed'] = True
        with col2:
            # Strike through text if completed
            if completed:
                st.markdown(f"~~{task_info['task']}~~")
            else:
                st.text(task_info['task'])
        with col3:
            # Button to remove task, with a unique key
            if st.button('Remove', key=f"remove-{i}"):
                # To avoid modifying the list directly, flag the item for removal
                st.session_state.checklist[i]['to_remove'] = True

    # Remove tasks flagged for removal
    st.session_state.checklist = [task for task in st.session_state.checklist if not task.get('to_remove', False)]

    # Optional: Clear all tasks button
    if st.button('Clear All Tasks'):
        st.session_state.checklist = []
