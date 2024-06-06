# Video Splitter

## Overview

The Video Splitter is a Python-based desktop application that allows users to split a video file into smaller segments of either 30 or 60 seconds. The application provides a simple graphical user interface (GUI) to select the input video file and the desired segment duration. The split segments are saved as separate video files in the same directory as the input video.

## Features

- Select an input video file to be split.
- Choose between 30-second or 60-second segments.
- Automatically splits the video into the specified segment duration.
- Saves each segment as a separate video file.

## Requirements

- Python 3.x
- tkinter
- moviepy

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/video-splitter.git
   cd video-splitter
   ```

2. **Install the required Python packages:**
   ```bash
   pip install moviepy
   ```

## Usage

1. **Run the application:**
   ```bash
   python video_splitter.py
   ```

2. **Use the application:**
   - Click the "Select" button to choose an input video file.
   - Select the desired segment duration (30 seconds or 60 seconds) by checking the appropriate checkbox.
   - Click the "Split Video" button to start the splitting process.
   - The split segments will be saved in the same directory as the input video file with filenames indicating the part number.

## Script Explanation

### Importing Libraries
```python
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip
```
- **os**: For file and directory operations.
- **tkinter**: For creating the graphical user interface.
- **moviepy**: For video processing and splitting.

### VideoSplitterApp Class
```python
class VideoSplitterApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Splitter")

        self.label = tk.Label(master, text="Select input video file:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select", command=self.select_file)
        self.select_button.pack()

        self.split_button = tk.Button(master, text="Split Video", command=self.split_video, state=tk.DISABLED)
        self.split_button.pack()

        self.check_var_30_sec = tk.IntVar()
        self.check_var_60_sec = tk.IntVar()

        self.check_30_sec = tk.Checkbutton(master, text="30 Second Segments", variable=self.check_var_30_sec)
        self.check_30_sec.pack()

        self.check_60_sec = tk.Checkbutton(master, text="60 Second Segments", variable=self.check_var_60_sec)
        self.check_60_sec.pack()
```
- Initializes the GUI components for selecting the input video file and segment duration.

### File Selection
```python
    def select_file(self):
        self.input_file_path = filedialog.askopenfilename()
        if self.input_file_path:
            self.split_button.config(state=tk.NORMAL)
```
- Allows the user to select the input video file and enables the "Split Video" button once a file is selected.

### Video Splitting
```python
    def split_video(self):
        base_name, ext = os.path.splitext(os.path.basename(self.input_file_path))

        video = VideoFileClip(self.input_file_path)
        duration = video.duration

        if self.check_var_30_sec.get():
            segment_duration = 30
        elif self.check_var_60_sec.get():
            segment_duration = 60
        else:
            messagebox.showerror("Error", "Please select a segment duration.")
            return

        num_segments = int(duration / segment_duration)

        for i in range(num_segments):
            start_time = i * segment_duration
            end_time = min((i + 1) * segment_duration, duration)
            output_file = f"{base_name}_part{i + 1}{ext}"

            subclip = video.subclip(start_time, end_time)
            subclip.write_videofile(output_file)

        # Handle the remaining duration for the last segment
        if duration % segment_duration != 0:
            start_time = num_segments * segment_duration
            end_time = duration
            output_file = f"{base_name}_part{num_segments + 1}{ext}"

            subclip = video.subclip(start_time, end_time)
            subclip.write_videofile(output_file)

        video.close()

        messagebox.showinfo("Success", "Video split successfully.")
```
- Splits the selected video into segments of the chosen duration and saves each segment with a filename indicating the part number.

### Main Window
```python
root = tk.Tk()
app = VideoSplitterApp(root)
root.mainloop()
```
- Sets up and runs the main event loop for the GUI.

## License

This project is licensed under the MIT License.
