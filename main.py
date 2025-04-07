import os
from download_models import download_models
import wx

def main(model_dir):
    if not os.path.exists(model_dir) or not os.listdir(model_dir):
        download_models(model_dir)
    wx.MessageBox("Models downloaded successfully!", "Info", wx.OK | wx.ICON_INFORMATION)

def start_app():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "The Vibes for Mac", size=(400, 200))
    panel = wx.Panel(frame, wx.ID_ANY)

    sizer = wx.BoxSizer(wx.VERTICAL)

    dir_picker = wx.DirPickerCtrl(panel, message="Select Models Directory")
    sizer.Add(dir_picker, 0, wx.ALL | wx.EXPAND, 5)

    start_button = wx.Button(panel, label="Start App")
    sizer.Add(start_button, 0, wx.ALL | wx.CENTER, 5)

    panel.SetSizer(sizer)

    def on_start(event):
        model_dir = dir_picker.GetPath()
        main(model_dir)

    start_button.Bind(wx.EVT_BUTTON, on_start)

    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    start_app()
