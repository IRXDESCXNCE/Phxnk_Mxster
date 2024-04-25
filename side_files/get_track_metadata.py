import eyed3
import os

def get_track_title(self, audio_file_path):
    audiofile = eyed3.load(audio_file_path)
    if audiofile.tag.title:
        self.title = audiofile.tag.title
        return self.title

    else:
        return os.path.basename(audio_file_path)

def get_track_artist(self, audio_file_path):
    audiofile = eyed3.load(audio_file_path)
    if audiofile.tag.artist:
        self.artist = audiofile.tag.artist
        return self.artist

    else:
        return("Unknown Artist")

def get_track_comment(self, audio_file_path):
    audiofile = eyed3.load(audio_file_path)
    if audiofile.tag.comments and audiofile.tag.comments[0] != None:
        return audiofile.tag.comments[0].text

    else:
        return ""