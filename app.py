# app.py — Simple To-Do List using Streamlit
import streamlit as st

st.set_page_config(page_title="Simple To-Do", layout="centered")
st.title("📝 Simple To-Do List")

# Initialize tasks in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []  # list of dicts: {"task": str, "done": bool}

# Input area to add a new task
with st.form("add_task_form", clear_on_submit=True):
    new_task = st.text_input("New task")
    submitted = st.form_submit_button("Add Task")
    if submitted and new_task.strip():
        st.session_state.tasks.append({"task": new_task.strip(), "done": False})
        st.success("Task added")

st.markdown("---")
st.subheader("Your tasks")

# Show tasks with Done / Delete buttons
if not st.session_state.tasks:
    st.info("No tasks yet — add one above!")
else:
    for i, item in enumerate(st.session_state.tasks):
        cols = st.columns([6, 1, 1])
        label = "✅ " + item["task"] if item["done"] else "🔲 " + item["task"]
        cols[0].write(label)
        if cols[1].button("Done", key=f"done_{i}"):
            st.session_state.tasks[i]["done"] = True
        if cols[2].button("Delete", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
