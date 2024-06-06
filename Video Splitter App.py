import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip

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

    def select_file(self):
        self.input_file_path = filedialog.askopenfilename()
        if self.input_file_path:
            self.split_button.config(state=tk.NORMAL)

    def split_video(self):
        base_name, ext = os.path.splitext(os.path.basename(self.input_file_path))

        video = VideoFileClip(self.input_file_path)
        duration = video.duration

        if self.check_var_30_sec.get():
            segment_duration = 30
        elif self.check_var_60_sec.get():
            segment_duration = 59
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


root = tk.Tk()
app = VideoSplitterApp(root)
root.mainloop()
