import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, SINGLE, END

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x300")

        pygame.mixer.init()

        self.playlist = []

        self.playlist_box = Listbox(self.root, selectmode=SINGLE)
        self.playlist_box.pack(fill="both", expand=True)

        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack(side="left")

        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack(side="left")

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_song)
        self.stop_button.pack(side="left")

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song)
        self.pause_button.pack(side="left")

        self.unpause_button = tk.Button(self.root, text="Unpause", command=self.unpause_song)
        self.unpause_button.pack(side="left")

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if song_path:
            song_name = os.path.basename(song_path)
            self.playlist.append(song_path)
            self.playlist_box.insert(END, song_name)

    def play_song(self):
        try:
            song_index = self.playlist_box.curselection()[0]
            song_path = self.playlist[song_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
        except IndexError:
            messagebox.showerror("Error", "No song selected.")

    def stop_song(self):
        pygame.mixer.music.stop()

    def pause_song(self):
        pygame.mixer.music.pause()

    def unpause_song(self):
        pygame.mixer.music.unpause()

def main():
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
