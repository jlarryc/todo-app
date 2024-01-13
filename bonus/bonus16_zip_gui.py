import PySimpleGUI as sg
import zip_creator

label1 = sg.Text("Select files to compress:")
input1 = sg.Input(key='-input-')
choose_button1 = sg.FilesBrowse("Choose", key='-files-')

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='-folder-')

compress_button = sg.Button("Compress", key='-compress-')
output_label = sg.Text(key='-output-')


window = sg.Window("File Zipper",
                   layout=[[label1,input1,choose_button1],
                           [label2,input2,choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    # get a list of file paths
    filepaths = values["-files-"].split(';')
    folderpath = values["-folder-"]
    match event:
        case "-compress-":
            print("I am compressing files")
            zip_creator.make_archive(filepaths, folderpath)
            window["-output-"].update(value="Compression completed!")

        case sg.WINDOW_CLOSED:
            break

window.close()
