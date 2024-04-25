import customtkinter
from .get_track_metadata import get_track_title, get_track_artist, get_track_comment

def add_tracks_in_playlist(self, master, paths):
    row = 0

    print("Adding new tracks")

    for track_path in paths:
        track_button = customtkinter.CTkButton(self.scrollable_frame, text=f"{get_track_artist(self, track_path)}   -   {get_track_title(self, track_path)}     {get_track_comment(self, track_path)}", command=lambda current_track=track_path: self.play_choosed_track(current_track))

        track_button.grid(row=row, column=0, pady=2)
        track_button.configure(width=800, height=40, corner_radius=0, fg_color="#242424", hover_color="#363636", text_color="grey", font=("Arial Bold", 16))

        self.track_path_list.append(track_path)

        print(f"added {track_path}")
        print("Tracks added")

        row += 1

    self.track_path_list = sorted(self.track_path_list)