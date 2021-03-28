# -*- coding: utf-8 -*-

# Author: 1dragosh

import os
import mutagen
from pydub import AudioSegment


musicfolder = '/path/to/Music/'
audio_extensions = ['.mp3']

files = []

for x in os.listdir(musicfolder):
    extension = os.path.splitext(x)[1]
    if extension in audio_extensions:
        files.append(x)

for x in files:
    bitrate = mutagen.File(musicfolder + x).info.bitrate / 1000
    if bitrate != 128.0:
        newfile = "bkup_" + x
        os.rename(musicfolder + x, musicfolder + newfile)
        os.system('sox "{}" -r 44100 "{}"'.format(musicfolder + newfile, musicfolder + x))
        os.remove(musicfolder + newfile)
        print("Remaining", len(files) - (files.index(x) + 1), "files. Last done:\n", x)

