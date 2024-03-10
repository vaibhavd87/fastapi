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
        # Checkbox to mark task as completed, with a unique key
        completed = st.checkbox("", key=f"chkbox-{i}", value=task_info['completed'])
    with col2:
        # Strike through text if completed
        if completed:
            st.markdown(f"~~{task_info['task']}~~")
            st.session_state.checklist[i]['completed'] = True
        else:
            st.text(task_info['task'])
    with col3:
        # Button to remove task, with a unique key
        if st.button('Remove', key=f"remove-{i}"):
            # To avoid modifying the list while iterating, flag the item for removal
            task_info['to_remove'] = True

# Remove tasks flagged for removal
st.session_state.checklist = [task for task in st.session_state.checklist if not task.get('to_remove', False)]

# Optional: Clear all tasks button
if st.button('Clear All Tasks'):
    st.session_state.checklist = []
