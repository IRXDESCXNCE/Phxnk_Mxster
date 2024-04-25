import customtkinter
import vlc
import json
import sys
from tkinter import filedialog
from PIL import Image
from side_files.get_track_metadata import get_track_title, get_track_artist, get_track_comment
from side_files.add_new_tracks import add_tracks_in_playlist
from side_files.time_counting import time_counting_cycle

class Phxnk_Mxster:
    def __init__(self):
        self.window = customtkinter.CTk()
        self.window.geometry("1000x850")
        self.window.title("Phxnk Mxster")
        self.tracks_on_main_frame_list = []
        self.button_list = []
        self.track_path_list = []
        self.track_names_list = []
        self.player = vlc.MediaPlayer()


    def initialize_interface(self):
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.window, width=800, height=700, fg_color="#080808")
        self.scrollable_frame.place(x=-1, y=-1)

        self.default_music_image = customtkinter.CTkImage(dark_image=Image.open("assets/default_music_icon.png"), size=(85, 85))
        self.lab = customtkinter.CTkLabel(self.window, image=self.default_music_image, text="")
        self.lab.place(x=100, y=737)

        self.next_button_image = customtkinter.CTkImage(dark_image=Image.open("assets/next.png"), size=(81, 78))
        self.next_button = customtkinter.CTkButton(self.window, image=self.next_button_image, width=82, height=82, corner_radius=0, text="", fg_color="transparent",hover_color="#636363")
        self.next_button.place(x=200, y=736)

        self.previous_button_image = customtkinter.CTkImage(dark_image=Image.open("assets/previous.png"), size=(81, 78))
        self.previous_button = customtkinter.CTkButton(self.window, image=self.previous_button_image, width=82, height=82, corner_radius=0, text="", fg_color="transparent", hover_color="#636363")
        self.previous_button.place(x=0, y=736)

        self.volume_slider = customtkinter.CTkSlider(self.window, from_=0, to=100, orientation="vertical", command=self.change_track_volume)
        self.volume_slider.place(x=950, y=580)

        try:
            with open('data/settings.json', 'r') as value:
                loaded_volume_data = json.load(value)
            volume_value = loaded_volume_data.get("volume")
            self.volume_slider.set(int(volume_value))

        except:
            self.volume_slider.set(0)

        print(f"Current colume - {volume_value}")

        self.time_slider = customtkinter.CTkSlider(self.window, from_=0, to=100, width=500)
        self.time_slider.place(x=300, y=760)
        #self.time_slider.bind("<ButtonRelease-1>", self.time_slider_change)
        self.time_slider.set(0)

        self.exit_button = customtkinter.CTkButton(self.window, text="Выход", command=sys.exit)
        self.exit_button.place(x=840, y=800)

        self.add_track_button = customtkinter.CTkButton(self.window, text="Добавить музыку", command=lambda: self.add_tracks_in_main_playlist())
        self.add_track_button.place(x=840, y=25)

        self.now_playing_track_label = customtkinter.CTkLabel(self.window, text="Сейчас играет: ", font=("Arial Bold", 16))
        self.now_playing_track_label.place(x=305, y=800)

        self.track_label = customtkinter.CTkLabel(self.window, text="")
        self.track_label.place(x=440, y=800)

        print("Interface initialized.")


    def add_tracks_in_main_playlist(self):
        paths_of_choosed_tracks = filedialog.askopenfilenames(title="Выберите треки", filetypes=[("Аудиофайлы", "*.mp3")])
        add_tracks_in_playlist(self, master=self.scrollable_frame, paths=paths_of_choosed_tracks)


    def play_choosed_track(self, current_track):
        self.player.stop()
        self.player = vlc.MediaPlayer(current_track)
        self.player.play()
        print(f"Player has started playing '{get_track_artist(self, audio_file_path=current_track)} - {get_track_title(self, audio_file_path=current_track)}'")


    def change_track_volume(self, value):
        self.player.audio_set_volume(int(value))
        print(f"Volume chaged to {int(value)}")

        with open('data/settings.json', 'r') as json_file:
            data = json.load(json_file)

        data['volume'] = int(value)

        with open('data/settings.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)


    def count_time(self):
        time_counting_cycle(self)


phxnk_mxster_app = Phxnk_Mxster()
phxnk_mxster_app.initialize_interface()
phxnk_mxster_app.window.mainloop()