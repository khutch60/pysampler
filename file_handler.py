from tkinter.filedialog import askopenfile, asksaveasfilename
import ast
import pygame as pg
from pitch_shift import PitchShift
import glob
import os
import re



class Samples:
    def __init__(self):
        self.samples = {}

        self.params = {}
    def new(self):
        self.params["bpm"] = 90
        self.params["steps"] = 16
        self.params["measures"] = 1
        self.samples = {}
        for x in range(8):
            self.samples[x] = [[{"sample": None,
                            "path": None,
                            "steps": [[False, False, 0] for x in range(64)],
                            "volume": 0.5,
                            "pitch": 0} for y in range(8)],
                          {"window": False, "mode": "drum"}]


    def save(self):
        save_dict = self.samples
        # for x in range(8):
        #     for sound in save_dict[x][0]:
        #         sound["sample"] = None
        string = {0: save_dict, 1: self.params}

        string = str(string)
        try:
            file = asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension="txt")
            file_save = open(file, 'w')
            file_save.write(string)
            file_save.close()

        except FileNotFoundError:
            pass




    def load(self):
        clear_all_temp_samples()
        pitch_shift = PitchShift()
        file = askopenfile(mode='r', filetypes=[("txt file", ".txt")])
        if file is not None:
            content = file.read()
            sound_object_loc = [i for i, letter in enumerate(content) if letter == "<"]
            # for char in content:
            #     try:
            #         index = content.index("<", start)
            #         sound_object_loc.append(index)
            #         start = index + 1
            #     except ValueError:
            #         break

            string_list = []
            for loc in sound_object_loc:
                string = ""
                for character in range(loc, loc + 49):
                    string += content[character]
                string_list.append(string)
            for string in string_list:
                content = content.replace(string, "None")

            new_dict = ast.literal_eval(content)

            self.samples = new_dict[0]
            self.params = new_dict[1]
            for x in range(8):
                for sample in self.samples[x][0]:
                    if sample["path"] is not None:
                        sample["sample"] = pg.mixer.Sound(sample["path"])

            for track in self.samples:
                for sample in range(8):
                    try:
                        self.samples[track][0][sample]["sample"].set_volume(self.samples[track][0][sample]["volume"])
                    except AttributeError:
                        pass
                    if self.samples[track][0][sample]["pitch"] > 0:
                        for x in range(self.samples[track][0][sample]["pitch"]):
                            self.samples[track][0][sample]["sample"] = pitch_shift.shift_up(track=track, sample=sample,
                                                                                       samples=self.samples)

                    elif self.samples[track][0][sample]["pitch"] < 0:
                        for x in range(self.samples[track][0][sample]["pitch"] * -1):
                            self.samples[track][0][sample]["sample"] = pitch_shift.shift_down(track=track, sample=sample,
                                                                                         samples=self.samples)








def clear_all_temp_samples():
    temp_files = glob.glob("temp-samples/*")
    for f in temp_files:
        os.remove(f)

def clear_one_sample(path):
    temp_files = glob.glob("temp-samples/*")
    for f in temp_files:
        if f == path:
            os.remove(f)
        os.remove(f)
#
# def save(samples, params):
#     # clear_all_temp_samples()
#     for x in range(8):
#         for sound in samples[x][0]:
#             sound["sample"] = None
#     string = {0: samples, 1: params}
#     string = str(string)
#     try:
#         file = asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension="txt")
#         file_save = open(file, 'w')
#         file_save.write(string)
#         file_save.close()
#     except FileNotFoundError:
#         pass