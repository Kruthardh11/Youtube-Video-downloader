import tkinter
import customtkinter
from tkinter import ttk
import yt_dlp

def update_progress(status):
    progress_var.set(status['downloaded_bytes'] / status['total_bytes'] * 100)
    app.update_idletasks()

def download_video():
    ytlink = link.get()
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [update_progress],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytlink])
        status_label.configure(text="Download complete", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Error: {e}", text_color="red")

def download_playlist():
    ytlink = link.get()
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': False,
        'progress_hooks': [update_progress],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytlink])
        status_label.configure(text="Playlist download complete", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Error: {e}", text_color="red")

def download_audio():
    ytlink = link.get()
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [update_progress],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytlink])
        status_label.configure(text="Audio download complete", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Error: {e}", text_color="red")

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame 
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(pady=(0, 20))

# Create a frame for buttons
button_frame = customtkinter.CTkFrame(app)
button_frame.pack(pady=(0, 20))

# Yellow Buttons
button_color = "#FFFF00"  # Yellow color

# Download Buttons
download_video_btn = tkinter.Button(button_frame, text="Download Video", command=download_video, bg=button_color, fg="black", font=("Arial", 12, "bold"))
download_video_btn.grid(row=0, column=0, padx=10, pady=10)

download_playlist_btn = tkinter.Button(button_frame, text="Download Playlist", command=download_playlist, bg=button_color, fg="black", font=("Arial", 12, "bold"))
download_playlist_btn.grid(row=0, column=1, padx=10, pady=10)

download_audio_btn = tkinter.Button(button_frame, text="Download Audio Only", command=download_audio, bg=button_color, fg="black", font=("Arial", 12, "bold"))
download_audio_btn.grid(row=0, column=2, padx=10, pady=10)

# Progress Bar
progress_var = tkinter.DoubleVar()
progress_bar = ttk.Progressbar(app, orient="horizontal", length=500, mode="determinate", variable=progress_var)
progress_bar.pack(pady=(20, 10))

# Status Label
status_label = customtkinter.CTkLabel(app, text="", text_color="black")
status_label.pack(pady=(10, 0))

# Run app
app.mainloop()
