import PySimpleGUI as  sg
from zip_functions import create_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
file_button1 = sg.FilesBrowse("choose files", key='files')

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
file_button2 = sg.FolderBrowse("select destination", key='folder')

compress_button = sg.Button("compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("file compressor",
                  layout=[[label1, input1, file_button1],
                  [label2, input2, file_button2],
                  [compress_button]])

while True: 
    event, values = window.read()
    print(event, values)

    filepaths = values["files"].split(";")
    folder = values["folder"]

    create_archive(filepaths, folder)
    window["output"].update(value="Compression complete")


window.close()



