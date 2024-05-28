import os
import tkinter as tk
import glob
import sys
from os import listdir
from os.path import isfile, join
from pathlib import Path
from tkinter import filedialog

from tinytag import TinyTag

if __name__ == '__main__':


    filetypes = ['flac','m4a','mp3','ogg','wav']
    project_root = Path(__file__).parent
    for type in filetypes:
        audio_files = glob.glob(f'*.{type}')
        if len(audio_files) == 0:
            continue
        !{sys.executable}

    print(project_root)
    print(audio_files)

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    print(file_path)
    filename, file_extension = os.path.splitext(file_path)
    print(file_extension)
    print(filename)

    tag = TinyTag.get(file_path)
    print(tag.samplerate)

    onlyfiles = [f for f in listdir(str(project_root)) if isfile(join(str(project_root), f))]
    print(onlyfiles)
