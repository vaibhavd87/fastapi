import streamlit as st

# Initialize session state to store the checklist
if 'checklist' not in st.session_state:
    st.session_state.checklist = []

# Title of the app
st.title('Checklist App')

# Text input for new task
new_task = st.text_input('Enter a task:', '')

# Button to add new task
if st.button('Add Task'):
    if new_task:  # Ensure the task is not empty
        st.session_state.checklist.append({'task': new_task, 'completed': False})
    else:
        st.warning('Please enter a task.')

# Display checklist
for i, task_info in enumerate(st.session_state.checklist):
    col1, col2, col3 = st.columns([0.05, 0.8, 0.15])
    with col1:
        # Checkbox to mark task as completed
        completed = st.checkbox("", key=str(i), value=task_info['completed'])
    with col2:
        # Strike through text if completed
        if completed:
            st.markdown(f"~~{task_info['task']}~~")
            st.session_state.checklist[i]['completed'] = True
        else:
            st.text(task_info['task'])
    with col3:
        # Button to remove task
        if st.button('Remove', key=str(i)):
            st.session_state.checklist.pop(i)

# Optional: Clear all tasks button
if st.button('Clear All Tasks'):
    st.session_state.checklist = []
