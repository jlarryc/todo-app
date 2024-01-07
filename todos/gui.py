import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window("ToDo App With a Very Long Title", layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()
print("Goodbye")
print(type(window))







