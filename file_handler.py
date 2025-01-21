from tkinter.filedialog import askopenfile, asksaveasfilename
import ast
import pygame as pg
from pitch_shift import PitchShift

class Samples:
    def __init__(self):
        self.samples = {}
        self.save_dict = self.samples
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
        self.save_dict = self.samples




    def save(self):
        self.save_dict = self.samples
        for x in range(8):
            for sound in self.save_dict[x][0]:
                sound["sample"] = None
        string = {0: self.save_dict, 1: self.params}

        string = str(string)
        try:
            file = asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension="txt")
            file_save = open(file, 'w')
            file_save.write(string)
            file_save.close()
        except FileNotFoundError:
            pass

    def load(self):
        pitch_shift = PitchShift()
        file = askopenfile(mode='r', filetypes=[("txt file", ".txt")])
        if file is not None:
            content = file.read()
            new_dict = ast.literal_eval(content)
            for x in range(8):
                for sample in new_dict[0][x][0]:
                    if sample["path"] is not None:
                        sample["sample"] = pg.mixer.Sound(sample["path"])

            for track in new_dict[0]:
                for sample in range(8):
                    try:
                        new_dict[0][track][0][sample]["sample"].set_volume(new_dict[0][track][0][sample]["volume"])
                    except AttributeError:
                        pass
                    if new_dict[0][track][0][sample]["pitch"] > 0:
                        for x in range(new_dict[0][track][0][sample]["pitch"]):
                            new_dict[0][track][0][sample]["sample"] = pitch_shift.shift_up(track=track, sample=sample,
                                                                                       samples=new_dict[0])

                    elif new_dict[0][track][0][sample]["pitch"] < 0:
                        for x in range(new_dict[0][track][0][sample]["pitch"] * -1):
                            new_dict[0][track][0][sample]["sample"] = pitch_shift.shift_down(track=track, sample=sample,
                                                                                         samples=new_dict[0])
            self.samples = new_dict[0]
            self.params = new_dict[1]





