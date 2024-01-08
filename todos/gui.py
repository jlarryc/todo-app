import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

# label2 = sg.Text("Edit a ToDo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("ToDo App With a Very Long Title",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font = ("Helvetica", 16))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()

            # values[todo_to_edit] = new_todo
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"

            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            values['todo'] = values['todos']
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:  # WIN_CLOSED is defined as None
            break

window.close()







