import streamlit as st
import functions

todos = functions.get_todos()
print(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# st.checkbox("Take morning pills.")
for todo in todos:
    st.checkbox(todo)
# st.checkbox("Take night pills")
# st.checkbox("Lock the doors.")

st.text_input(label="Todo: ", placeholder='Add a new todo...', on_change=functions.write_todos(todos, "todos.txt"))
