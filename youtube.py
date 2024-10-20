# Importing the necessary libraries
from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog  # For graphical user output

# Function to download the video from a given URL to the specified save path
def download_video(url, save_path):
    try:
        yt = YouTube(url)  # Create an instance of the YouTube video
        streams = yt.streams.filter(progressive=True, file_extension='mp4')  # Filter for progressive mp4 streams
        highest_res_stream = streams.get_highest_resolution()  # Get the highest resolution stream
        highest_res_stream.download(output_path=save_path)  # Download the video to the specified path
        print("Video downloaded!")  # Success message

    except Exception as e:
        print(e)  # Print any error that occurs during the download

# Function to open a file dialog for selecting a save directory
def open_file_dialog():
    folder = filedialog.askdirectory()  # Open the directory selection dialog
    if folder:
        print(f"Selected Folder: {folder}")  # Print the selected folder

    return folder  # Return the selected folder path

# Main execution block
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    root.withdraw()  # Hide the main window (we're using console input for URL)

    video_url = input("Please enter a Youtube url: ")  # Get the video URL from user input
    save_dir = open_file_dialog()  # Open the dialog to select save directory

    if not save_dir:  # Check if a valid save location was selected
        print("Invalid save location!")
    else:
        print("Started Download!")  # Indicate that the download process is starting
        download_video(video_url, save_dir)  # Call the download function with the provided URL and save path
