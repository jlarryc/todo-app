import functions
import PySimpleGUI as sg
import time
import random

# sg.theme("Dark Teal 5")
# sg.theme("Sandy Beach")


my_theme = ["Black","DarkGrey10","DarkTeal5", "SandyBeach","LightGreen1","LightGreen2",
            "LightGreen3","LightBrown1","LightBrown2","LightBrown3","LightBrown4","Tan",
            "Kayak","TanBlue","Purple","DarkPurple4","DarkRed"]

my_rand = random.randrange(0, len(my_theme))
print(f"Current Theme is: {my_rand}:{sg.theme(my_theme[my_rand])}")


time_label = sg.Text("",key='date_time')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo", size=(45))
# add_button = sg.Button("Add", size=20)
add_button = sg.Button(image_source="add.png", image_size=(40,40),key='-add-',
                       tooltip="Add", mouseover_colors="LightBlue2")

# label2 = sg.Text("Edit a ToDo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")

# checkoff_button = sg.Button("Complete")
checkoff_button = sg.Button(image_source="complete.png", key='-checkoff-', image_size=(40,40), tooltip="Complete")

delete_button = sg.Button("Delete")

exit_button = sg.Button("Exit")



window = sg.Window("ToDo App",
                   layout=[[time_label],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, checkoff_button, delete_button],
                        [exit_button]],
                   font = ("Helvetica", 16))
while True:
    event, values = window.read(timeout=200)
    # event, values = window.read()
    window['date_time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(0,event, values)
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case '-add-':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                new_todo = new_todo

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError as e:
                sg.popup(title="Error",custom_text="Must select a todo item to edit!",font=("Helvetica", 16))
                print(f"{e}: Must select a todo item to edit!")

        case '-checkoff-':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = f"\u2714 {values['todo']}"
                todos = functions.get_todos()

                # values[todo_to_edit] = new_todo
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                functions.write_todos(todos)
                window['todos'].update(values=todos)

                """ *** TRY THIS START *** """
                """
                todo_to_edit = values['todos'][0]
                # new_todo = f"|X| {values['todo']}"
                new_todo = f"{values['todo']}"
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                """


                # window['todo'].update("")
                # window['todo'].update(value=values['todo'][0])
                # window['todo'].update(value=values['todo'])
                """ *** TRY THIS END *** """
            except IndexError as e:
                sg.popup(title="Error",custom_text="Must select a todo item to mark as completed!",font=("Helvetica", 16))
                print(f"{e}: Must select a todo item to mark as completed!")
            """ EXPERIMENTAL 2ND TRY / EXCEPT BLOCK START """
            try:
                print("SECOND TRY!")
                values['todo'] = values['todos']
                # window['todo'].update(value=values['todos'][0])
            except IndexError as e:
                sg.popup(title="Error", custom_text="Must select a todo item to mark as completed!",
                         font=("Helvetica", 16))
                print(f"{e}: Must select a todo item to mark as completed!")
            """ EXPERIMENTAL 2ND TRY / EXCEPT BLOCK START """

        case "Delete":
            try:
                todo_to_delete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError as e:
                sg.popup(title="Error",custom_text="Must select a todo item to be deleted!",font=("Helvetica", 16))
                print(f"{e}: Must select a todo item to be deleted!")
        case 'todos':
            values['todo'] = values['todos']
            window['todo'].update(value=values['todos'][0])
        # case 'date_time':
        #     values['date_time'] = f"{time.strftime("%H%M%S")}"
        #     window['date_time'].update(value=f"{time.strftime('%H%M%S')}")
        case "Exit":
            break
        case sg.WIN_CLOSED:  # WIN_CLOSED is defined as None
            break

window.close()







