import os
from huggingface_hub import hf_hub_download
import wx

def download_models(model_dir):
    model_ids = [
        "openai/whisper-small",
        "facebook/wav2vec2-base-960h"
    ]

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Downloading Models", size=(400, 200))
    panel = wx.Panel(frame, wx.ID_ANY)

    sizer = wx.BoxSizer(wx.VERTICAL)
    text = wx.StaticText(panel, label="Downloading models, please wait...")
    sizer.Add(text, 0, wx.ALL | wx.CENTER, 5)

    progress_bar = wx.Gauge(panel, range=len(model_ids), size=(250, 25))
    sizer.Add(progress_bar, 0, wx.ALL | wx.CENTER, 5)

    panel.SetSizer(sizer)
    frame.Show(True)

    for i, model_id in enumerate(model_ids):
        try:
            model_path = hf_hub_download(repo_id=model_id, filename="pytorch_model.bin", cache_dir=model_dir)
            print(f"Downloaded {model_id} to {model_path}")
        except Exception as e:
            print(f"Failed to download {model_id}: {e}")
        progress_bar.SetValue(i + 1)
        wx.Yield()

    wx.MessageBox("Models downloaded successfully!", "Info", wx.OK | wx.ICON_INFORMATION)
    frame.Close()

if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "The Vibes for Mac", size=(400, 200))
    panel = wx.Panel(frame, wx.ID_ANY)

    sizer = wx.BoxSizer(wx.VERTICAL)

    text = wx.StaticText(panel, label="Select Models Directory")
    sizer.Add(text, 0, wx.ALL | wx.CENTER, 5)

    dir_picker = wx.DirPickerCtrl(panel, message="Select Models Directory")
    sizer.Add(dir_picker, 0, wx.ALL | wx.EXPAND, 5)

    download_button = wx.Button(panel, label="Download Models")
    sizer.Add(download_button, 0, wx.ALL | wx.CENTER, 5)

    panel.SetSizer(sizer)

    def on_download(event):
        model_dir = dir_picker.GetPath()
        download_models(model_dir)

    download_button.Bind(wx.EVT_BUTTON, on_download)

    frame.Show(True)
    app.MainLoop()
