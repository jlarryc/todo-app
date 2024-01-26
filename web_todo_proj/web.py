import streamlit as st
import functions

DEBUG = True

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['-new_todo-'] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos,"todos.txt")

    # st.text_input("")


def delete_todo(idx):
    del_todo = st.session_state[todo]
    print(del_todo)
    print("I want to delete this todo!")
    todos.pop(idx)
    functions.write_todos(todos)
    del st.session_state[todo]  # removes from st.session_state dictionary
    st.rerun()  # refreshes the todo list as displayed
def complete_todo(idx):
    comp_todo = '[X] ' + todo
    print("TODO COMPLETED: ", todo)
    todos[idx] = comp_todo
    functions.write_todos(todos)

print(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# st.checkbox("Take morning pills.")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        # delete_todo(index)
        complete_todo(index)
    # if deletebox:
    #     delete_todo(index)
# st.checkbox("Take night pills")
# st.checkbox("Lock the doors.")

st.text_input(label="Todo: ", placeholder='Add a new todo...',
              key='-new_todo-', on_change=add_todo)


#For Debug: This statement will display the session_state
if DEBUG:
    st.session_state