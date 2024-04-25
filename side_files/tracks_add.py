from tkinter import filedialog
import customtkinter


def add_track_in_main_playlist(self, window):
    row = 0
    choosed_tracks = filedialog.askopenfilenames(title="Выберите аудиофайлы", filetypes=[("Аудиофайлы", "*.mp3")])
    self.tracks_info = []

    for track in choosed_tracks:

        if not self.get_track_title(track) in self.tracks_info and not self.get_track_artist(track) in self.tracks_info:
            self.tracks_info.append(self.tracks_info)

            self.track_button = customtkinter.CTkButton(window, text=f"{self.get_track_artist(audio_file_path=track)}    -    {self.get_track_title(audio_file_path=track)}  {self.get_track_comment(audio_file_path=track)}")
            self.track_button.configure(width=800, height=40, text_color="#808080", fg_color="#242424", hover_color="#363636", corner_radius=0, font=("Arial Bold", 16), command=lambda path=track: self.play_choosed_track(path))
            self.track_button.grid(row=row, column=0, pady=2)

            self.main_playlist.append(track)
            self.main_playlist = sorted(self.main_playlist)

            row += 1

