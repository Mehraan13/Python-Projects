''' Youtube Video Downloader '''

from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog # for graphical user output

def download_video(url, save_path):
    try:
       yt = YouTube(url) # grab an instance of the video
       streams = yt.streams.filter(progressive = True, file_extension = 'mp4')
       highest_res_stream = streams.get_highest_resolution()
       highest_res_stream.download(output_path = save_path)
       print("Video downloaded!")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() # hide the window

    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location! ")
    else:
        print("Started Download! ")
        download_video(video_url, save_dir)