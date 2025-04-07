import os
from huggingface_hub import hf_hub_download
import PySimpleGUI as sg

def download_models(model_dir):
    model_ids = [
        "openai/whisper-small",
        "facebook/wav2vec2-base-960h"
    ]

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    layout = [
        [sg.Text("Downloading models, please wait...")],
        [sg.ProgressBar(len(model_ids), orientation='h', size=(20, 20), key='-PROGRESS-')]
    ]

    window = sg.Window("Downloading Models", layout)

    progress_bar = window['-PROGRESS-']

    for i, model_id in enumerate(model_ids):
        try:
            model_path = hf_hub_download(repo_id=model_id, filename="pytorch_model.bin", cache_dir=model_dir)
            print(f"Downloaded {model_id} to {model_path}")
        except Exception as e:
            print(f"Failed to download {model_id}: {e}")
        progress_bar.UpdateBar(i + 1)
        window.refresh()

    window.close()

if __name__ == "__main__":
    layout = [
        [sg.Text("Select Models Directory")],
        [sg.Input(key="-FOLDER-"), sg.FolderBrowse()],
        [sg.Button("Download Models")]
    ]

    window = sg.Window("The Vibes for Mac", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Download Models":
            model_dir = values["-FOLDER-"]
            download_models(model_dir)

    window.close()
