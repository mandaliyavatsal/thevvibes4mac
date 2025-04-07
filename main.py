import os
from download_models import download_models
import PySimpleGUI as sg

def main(model_dir):
    if not os.path.exists(model_dir) or not os.listdir(model_dir):
        download_models(model_dir)
    sg.popup("Models downloaded successfully!")

def start_app():
    layout = [
        [sg.Text("Select Models Directory")],
        [sg.Input(key="-FOLDER-"), sg.FolderBrowse()],
        [sg.Button("Start App")]
    ]

    window = sg.Window("The Vibes for Mac", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Start App":
            model_dir = values["-FOLDER-"]
            main(model_dir)

    window.close()

if __name__ == "__main__":
    start_app()
