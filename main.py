from metronome import Clock
import os
import glob
import pygame as pg
import tkinter
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment



temp_files = glob.glob("temp-samples/*")
for f in temp_files:
    os.remove(f)

tkinter.Tk().withdraw()

pg.init()
pg.font.init()

pg.display.set_caption('PySampler')
image = pg.image.load("icon.png")
pg.display.set_icon(image)
window_surface = pg.display.set_mode((1000, 600))

pygame_clock = pg.time.Clock()

is_running = True


# Sample playback tracking
samples = {
    1: {
        1:
            {"sample": pg.mixer.Sound("samples/synthwave-kick-punch_C_minor.wav"),
             "path": "samples/synthwave-kick-punch_C_minor.wav",
             "steps": {1: [True, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [True, False, 0], 8: [False, False, 0],
                       9: [True, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [True, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [True, False, 0], 16: [False, False, 0],
                       17: [True, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [True, False, 0], 24: [False, False, 0],
                       25: [True, False, 0], 26: [False, False, 0], 27: [False, False, 0], 28: [True, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [True, False, 0], 32: [False, False, 0],
                       33: [True, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [True, False, 0], 40: [False, False, 0],
                       41: [True, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [True, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [True, False, 0], 48: [False, False, 0],
                       49: [True, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [True, False, 0], 56: [False, False, 0],
                       57: [True, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [True, False, 0],
                       61: [True, False, 0], 62: [True, False, 0], 63: [True, False, 0], 64: [True, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        2:
            {"sample": pg.mixer.Sound("samples/origin-snare.wav"),
             "path": "samples/origin-snare.wav",
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [True, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [True, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [True, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False, 0], 28: [False, False, 0],
                       29: [True, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [True, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [True, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [True, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [True, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        3:
            {"sample": pg.mixer.Sound("samples/hat 1.wav"),
             "path": "samples/hat 1.wav",
             "steps": {1: [True, False, 0], 2: [False, False, 0], 3: [True, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False], 7: [True, False], 8: [False, False],
                       9: [False, False, 0], 10: [False, False, 0], 11: [True, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [True, False, 0], 16: [False, False, 0],
                       17: [True, False, 0], 18: [False, False, 0], 19: [True, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [True, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [True, False, 0], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [True, False, 0], 32: [False, False, 0],
                       33: [True, False, 0], 34: [False, False, 0], 35: [True, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [True, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [True, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [True, False, 0], 48: [False, False, 0],
                       49: [True, False, 0], 50: [False, False, 0], 51: [True, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [True, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [True, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [True, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        4:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        5:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        6:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        7:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        8:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        "window": True,
        "mode": "drum"
        },
    2: {
        1:
            {"sample": pg.mixer.Sound("samples/analog-synth-bass-poison_C_major.wav"),
             "path": "samples/analog-synth-bass-poison_C_major.wav",
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        2:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 0.5,
             "pitch": 0},
        3:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        4:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        5:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        6:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        7:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        8:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        "window": False,
        "mode": "instrument"
        },
    3: {
        1:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        2:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        3:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        4:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        5:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        6:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        7:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        8:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        "window": False,
        "mode": "instrument"
        },
    4: {
        1:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        2:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        3:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        4:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        5:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        6:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        7:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        8:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        "window": False,
        "mode": "drum"
        },
    5: {
        1:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        2:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        3:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        4:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        5:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        6:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False], 2: [False, False], 3: [False, False], 4: [False, False],
                       5: [False, False], 6: [False, False], 7: [False, False], 8: [False, False],
                       9: [False, False], 10: [False, False], 11: [False, False], 12: [False, False],
                       13: [False, False], 14: [False, False], 15: [False, False], 16: [False, False],
                       17: [False, False], 18: [False, False], 19: [False, False], 20: [False, False],
                       21: [False, False], 22: [False, False], 23: [False, False], 24: [False, False],
                       25: [False, False], 26: [False, False], 27: [False, False], 28: [False, False],
                       29: [False, False], 30: [False, False], 31: [False, False], 32: [False, False],
                       33: [False, False], 34: [False, False], 35: [False, False], 36: [False, False],
                       37: [False, False], 38: [False, False], 39: [False, False], 40: [False, False],
                       41: [False, False], 42: [False, False], 43: [False, False], 44: [False, False],
                       45: [False, False], 46: [False, False], 47: [False, False], 48: [False, False],
                       49: [False, False], 50: [False, False], 51: [False, False], 52: [False, False],
                       53: [False, False], 54: [False, False], 55: [False, False], 56: [False, False],
                       57: [False, False], 58: [False, False], 59: [False, False], 60: [False, False],
                       61: [False, False], 62: [False, False], 63: [False, False], 64: [False, False]
                       },
             "volume": 1.0,
             "pitch": 0},
        7:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False], 2: [False, False], 3: [False, False], 4: [False, False],
                       5: [False, False], 6: [False, False], 7: [False, False], 8: [False, False],
                       9: [False, False], 10: [False, False], 11: [False, False], 12: [False, False],
                       13: [False, False], 14: [False, False], 15: [False, False], 16: [False, False],
                       17: [False, False], 18: [False, False], 19: [False, False], 20: [False, False],
                       21: [False, False], 22: [False, False], 23: [False, False], 24: [False, False],
                       25: [False, False], 26: [False, False], 27: [False, False], 28: [False, False],
                       29: [False, False], 30: [False, False], 31: [False, False], 32: [False, False],
                       33: [False, False], 34: [False, False], 35: [False, False], 36: [False, False],
                       37: [False, False], 38: [False, False], 39: [False, False], 40: [False, False],
                       41: [False, False], 42: [False, False], 43: [False, False], 44: [False, False],
                       45: [False, False], 46: [False, False], 47: [False, False], 48: [False, False],
                       49: [False, False], 50: [False, False], 51: [False, False], 52: [False, False],
                       53: [False, False], 54: [False, False], 55: [False, False], 56: [False, False],
                       57: [False, False], 58: [False, False], 59: [False, False], 60: [False, False],
                       61: [False, False], 62: [False, False], 63: [False, False], 64: [False, False]
                       },
             "volume": 1.0,
             "pitch": 0},
        8:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        "window": False,
        "mode": "drum"
        },
    6: {
        1:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        2:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        3:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        4:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        5:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        6:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        7:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        8:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        "window": False,
        "mode": "drum"
        },
    7: {
        1:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        2:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        3:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        4:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        5:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        6:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        7:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        8:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        "window": False,
        "mode": "drum"
        },
    8: {
        1:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        2:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        3:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        4:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        5:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        6:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        7:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        8:
            {"sample": None,
             "path": None,
             "steps": {1: [False, False, 0], 2: [False, False, 0], 3: [False, False, 0], 4: [False, False, 0],
                       5: [False, False, 0], 6: [False, False, 0], 7: [False, False, 0], 8: [False, False, 0],
                       9: [False, False, 0], 10: [False, False, 0], 11: [False, False, 0], 12: [False, False, 0],
                       13: [False, False, 0], 14: [False, False, 0], 15: [False, False, 0], 16: [False, False, 0],
                       17: [False, False, 0], 18: [False, False, 0], 19: [False, False, 0], 20: [False, False, 0],
                       21: [False, False, 0], 22: [False, False, 0], 23: [False, False, 0], 24: [False, False, 0],
                       25: [False, False, 0], 26: [False, False, 0], 27: [False, False], 28: [False, False, 0],
                       29: [False, False, 0], 30: [False, False, 0], 31: [False, False, 0], 32: [False, False, 0],
                       33: [False, False, 0], 34: [False, False, 0], 35: [False, False, 0], 36: [False, False, 0],
                       37: [False, False, 0], 38: [False, False, 0], 39: [False, False, 0], 40: [False, False, 0],
                       41: [False, False, 0], 42: [False, False, 0], 43: [False, False, 0], 44: [False, False, 0],
                       45: [False, False, 0], 46: [False, False, 0], 47: [False, False, 0], 48: [False, False, 0],
                       49: [False, False, 0], 50: [False, False, 0], 51: [False, False, 0], 52: [False, False, 0],
                       53: [False, False, 0], 54: [False, False, 0], 55: [False, False, 0], 56: [False, False, 0],
                       57: [False, False, 0], 58: [False, False, 0], 59: [False, False, 0], 60: [False, False, 0],
                       61: [False, False, 0], 62: [False, False, 0], 63: [False, False, 0], 64: [False, False, 0]
                       },
             "volume": 1.0,
             "pitch": 0},
        "window": False,
        "mode": "drum"
        },

    }


pg.mixer.set_num_channels(30)


def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


note_half_step_up = 1.05946
note_half_step_down = 0.94054

step = 1
clock = Clock()

bpm = 80
step_length = ((60/bpm) / 4)
clock.step_length = step_length
audio_start = False

light_step = 1
light_x_pos = -10

step_total = 64
measure_number = 1
measure_total = 4

start_button_press = False
volume_adjust = True
mouse_hold = False
row_click = None
pad_hover = None
original_pad = None
original_x = None
pad_hover_x = None


recording = False

start_font = pg.font.SysFont('Arial', 20)
start_text = start_font.render("Play", False, "#555555")

record_font = pg.font.SysFont('Arial', 20)
record_text = record_font.render("Record", False, "#555555")

back_font = pg.font.SysFont('Arial', 20)
back_text = back_font.render("Back", False, "#555555")

select_font = pg.font.SysFont('Arial', 20)
text_surface = select_font.render('Select', False, "white")

up_down_font = pg.font.SysFont('Arial', 10)
up_text = up_down_font.render('Up', False, "white")
down_text = up_down_font.render('Down', False, "white")

volume_font = pg.font.SysFont('Arial', 15)
volume_text = volume_font.render('Volume', False, "white")

bpm_font = pg.font.SysFont('Arial', 30)
bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")

measure_font = pg.font.SysFont('Arial', 30)
measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")

step_font = pg.font.SysFont('Arial', 30)
step_text = measure_font.render(f"Step Count: {step_total}", False, "white")

track_font = pg.font.SysFont('Arial', 30)
track_text = track_font.render("Track:", False, "white")
# track_numbers = [track_font.render(f'{number + 1}', False, "white") for number in range(8)]
track_numbers = {
    1: track_font.render('1', False, "white"),
    2: track_font.render('2', False, "white"),
    3: track_font.render('3', False, "white"),
    4: track_font.render('4', False, "white"),
    5: track_font.render('5', False, "white"),
    6: track_font.render('6', False, "white"),
    7: track_font.render('7', False, "white"),
    8: track_font.render('8', False, "white"),
}

track_view = 1

for track in range(8):
    if samples[track + 1]["window"]:
        track_view = track + 1

track_numbers[track_view] = track_font.render(f"{track_view}", False, "#555555")

for track in samples:
    for sample in range(8):
        try:
            samples[track][sample + 1]["sample"].set_volume(samples[track][sample + 1]["volume"])
        except AttributeError:
            pass
        if samples[track][sample + 1]["pitch"] > 0:
            for x in range(samples[track][sample + 1]["pitch"]):
                try:
                    path = f"temp-samples/track {track} row {sample + 1}.wav"
                    audio = AudioSegment.from_file(path)

                except FileNotFoundError:
                    samples[track][sample + 1]["pitch"] += 1
                    path = samples[track][sample + 1]["path"]
                    audio = AudioSegment.from_file(path)
                slow_sound = speed_change(sound=audio, speed=note_half_step_up)
                slow_sound.export(f"temp-samples/track {track} row {sample + 1}.wav", format="wav")
                samples[track][sample + 1]["sample"] = pg.mixer.Sound(
                    f"temp-samples/track {track} row {sample + 1}.wav")
                samples[track][sample + 1]["sample"].set_volume(samples[track][sample + 1]["volume"])
        elif samples[track][sample + 1]["pitch"] < 0:
            for x in range(samples[track][sample + 1]["pitch"]):
                try:
                    path = f"temp-samples/track {track} row {sample + 1}.wav"
                    audio = AudioSegment.from_file(path)

                except FileNotFoundError:
                    samples[track][sample + 1]["pitch"] += 1
                    path = samples[track][sample + 1]["path"]
                    audio = AudioSegment.from_file(path)
                slow_sound = speed_change(sound=audio, speed=note_half_step_down)
                slow_sound.export(f"temp-samples/track {track} row {sample + 1}.wav", format="wav")
                samples[track][sample + 1]["sample"] = pg.mixer.Sound(
                    f"temp-samples/track {track} row {sample + 1}.wav")
                samples[track][sample + 1]["sample"].set_volume(samples[track][sample + 1]["volume"])


def play():
    global samples, clock, light_step, light_x_pos, step
    if clock.step():
        if light_step > 16:
            light_step = 1
            light_x_pos = 65
        if step > step_total:
            step = 1
        for tracks in range(8):
            if samples[tracks + 1]["mode"] == "drum":
                for sample in range(8):
                    if samples[tracks + 1][sample + 1]["steps"][step][0]:
                        try:
                            samples[tracks + 1][sample + 1]["sample"].stop()
                            samples[tracks + 1][sample + 1]["sample"].play()
                        except AttributeError:
                            pass
            elif samples[tracks + 1]["mode"] == "instrument":
                for sample in range(8):
                    try:
                        if samples[tracks + 1][sample + 1]["steps"][step][1]:
                            pass
                        else:
                            samples[tracks + 1][sample + 1]["sample"].stop()
                    except AttributeError:
                        pass
                    if samples[tracks + 1][sample + 1]["steps"][step][0]:
                        try:
                            samples[tracks + 1][sample + 1]["sample"].play(loops=-1)

                        except AttributeError:
                            pass
        step += 1
        light_step += 1
        light_x_pos += 50


while is_running:
    if recording:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if record_button.x < pg.mouse.get_pos()[0] < (record_button.x + 70):
                    if record_button.y < pg.mouse.get_pos()[1] < (record_button.y + 30):
                        recording = False

        if audio_start:
            play()

        window_surface.fill("#555555")

        record_button = pg.draw.rect(surface=window_surface,
                                             color="white",
                                             rect=(900, 35, 70, 30),
                                             width=0)
        window_surface.blit(back_text, (913, 38))
        pg.display.flip()
    elif samples[track_view]["mode"] == "drum":
        for event in pg.event.get():
            if event.type == pg.QUIT:

                is_running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                # Start button press
                if 900 < pg.mouse.get_pos()[0] < 970:
                    if 550 < pg.mouse.get_pos()[1] < 580:
                        start_button_press = True

                # Record button press
                if record_button.x < pg.mouse.get_pos()[0] < (record_button.x + 70):
                    if record_button.y < pg.mouse.get_pos()[1] < (record_button.y + 30):
                        recording = True

                # Volume or pitch
                if volume_pitch_button.x < pg.mouse.get_pos()[0] < (volume_pitch_button.x + 70):
                    if volume_pitch_button.y < pg.mouse.get_pos()[1] < (volume_pitch_button.y + 20):
                        if volume_adjust:
                            volume_adjust = False
                        else:
                            volume_adjust = True

                # Pad press
                for row in range(len(rows)):
                    for pad in range(len(rows[1])):
                        if rows[row + 1][pad].x < pg.mouse.get_pos()[0] < (rows[row + 1][pad].x + 30):
                            if rows[row + 1][pad].y < pg.mouse.get_pos()[1] < (rows[row + 1][pad].y + 30):
                                if step > 47:
                                    pad += 48
                                elif step > 31:
                                    pad += 32
                                elif step > 15:
                                    pad += 16
                                else:
                                    pass
                                if samples[track_view][row + 1]["steps"][pad + 1][0]:
                                    samples[track_view][row + 1]["steps"][pad + 1][0] = False
                                else:
                                    samples[track_view][row + 1]["steps"][pad + 1][0] = True
                                    try:
                                        samples[track_view][row + 1]["sample"].play()
                                    except AttributeError:
                                        pass

                    # Sample select press

                    if sample_select[row + 1].x < pg.mouse.get_pos()[0] < (sample_select[row + 1].x + 70):
                        if sample_select[row + 1].y < pg.mouse.get_pos()[1] < (sample_select[row + 1].y + 30):
                            try:
                                sample = askopenfilename()

                                try:
                                    samples[track_view][row + 1]["sample"].fadeout(500)
                                except AttributeError:
                                    pass

                                for f in temp_files:
                                    if f == f"temp-samples\\track {track_view} row {row + 1}.wav":
                                        os.remove(f)
                                samples[track_view][row + 1]["path"] = sample
                                samples[track_view][row + 1]["sample"] = pg.mixer.Sound(sample)
                                samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])

                            except FileNotFoundError:
                                pass

                    # Volume/pitch adjust

                    if sample_volume[row + 1][0].x < pg.mouse.get_pos()[0] < (sample_volume[row + 1][0].x + 60):
                        if sample_volume[row + 1][0].y < pg.mouse.get_pos()[1] < (sample_volume[row + 1][0].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][row + 1]["volume"] == 1.0:
                                        pass
                                    else:
                                        samples[track_view][row + 1]["volume"] = samples[track_view][row + 1]["volume"] + .1
                                        samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])
                                else:
                                    try:
                                        path = f"temp-samples/track {track_view} row {row + 1}.wav"
                                        audio = AudioSegment.from_file(path)

                                    except FileNotFoundError:
                                        samples[track_view][row + 1]["pitch"] += 1
                                        path = samples[track_view][row+1]["path"]
                                        audio = AudioSegment.from_file(path)
                                    fast_sound = speed_change(sound=audio, speed=note_half_step_up)

                                    fast_sound.export(f"temp-samples/track {track_view} row {row+1}.wav", format="wav")
                                    samples[track_view][row + 1]["sample"] = pg.mixer.Sound(f"temp-samples/track {track_view} row {row+1}.wav")
                                    samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])
                            except AttributeError:
                                pass

                    if sample_volume[row + 1][1].x < pg.mouse.get_pos()[0] < (sample_volume[row + 1][1].x + 60):
                        if sample_volume[row + 1][1].y < pg.mouse.get_pos()[1] < (sample_volume[row + 1][1].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][row + 1]["volume"] == 0:
                                        pass
                                    else:
                                        samples[track_view][row + 1]["volume"] = samples[track_view][row + 1]["volume"] - .1
                                        samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])
                                else:
                                    try:
                                        path = f"temp-samples/track {track_view} row {row + 1}.wav"
                                        audio = AudioSegment.from_file(path)

                                    except FileNotFoundError:
                                        samples[track_view][row + 1]["pitch"] += 1
                                        path = samples[track_view][row+1]["path"]
                                        audio = AudioSegment.from_file(path)

                                    slow_sound = speed_change(sound=audio, speed=note_half_step_down)
                                    slow_sound.export(f"temp-samples/track {track_view} row {row+1}.wav", format="wav")
                                    samples[track_view][row + 1]["sample"] = pg.mixer.Sound(f"temp-samples/track {track_view} row {row + 1}.wav")
                                    samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])
                            except AttributeError:
                                pass

                # Bpm adjust
                if bpm_buttons[0].x < pg.mouse.get_pos()[0] < (bpm_buttons[0].x + 15):
                    if bpm_buttons[0].y < pg.mouse.get_pos()[1] < (bpm_buttons[0].y + 15):
                        bpm += 1
                        step_length = (60 / bpm) / 4
                        clock.step_length = step_length
                        bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
                if bpm_buttons[1].x < pg.mouse.get_pos()[0] < (bpm_buttons[1].x + 15):
                    if bpm_buttons[1].y < pg.mouse.get_pos()[1] < (bpm_buttons[1].y + 15):
                        bpm -= 1
                        step_length = (60 / bpm) / 4
                        clock.step_length = step_length
                        bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")

                # Measure select
                if measure_buttons[0].x < pg.mouse.get_pos()[0] < (measure_buttons[0].x + 15):
                    if measure_buttons[0].y < pg.mouse.get_pos()[1] < (measure_buttons[0].y + 15):
                        # step += 16
                        if step < 49:
                            if step <= step_total:
                                step += 17

                        else:
                            pass

                if measure_buttons[1].x < pg.mouse.get_pos()[0] < (measure_buttons[1].x + 15):
                    if measure_buttons[1].y < pg.mouse.get_pos()[1] < (measure_buttons[1].y + 15):
                        if step > 16:
                            step -= 16
                        else:
                            pass

                # Step adjust
                if step_buttons[0].x < pg.mouse.get_pos()[0] < (step_buttons[0].x + 15):
                    if step_buttons[0].y < pg.mouse.get_pos()[1] < (step_buttons[0].y + 15):
                        if step_total == 64:
                            pass
                        else:
                            step_total += 16
                            measure_total += 1
                            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                            step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                            # step = 1

                if step_buttons[1].x < pg.mouse.get_pos()[0] < (step_buttons[1].x + 15):
                    if step_buttons[1].y < pg.mouse.get_pos()[1] < (step_buttons[1].y + 15):
                        if step_total == 16:
                            pass
                        else:
                            step_total -= 16
                            measure_total -= 1
                            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                            step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                            # step = 1

                # Track select
                for button in range(8):
                    if track_select[button].x < pg.mouse.get_pos()[0] < (track_select[button].x + 30):
                        if track_select[button].y < pg.mouse.get_pos()[1] < (track_select[button].y + 30):
                            track_numbers[track_view] = track_font.render(f'{track_view}', False, "White")
                            samples[track_view]["window"] = False
                            track_view = button + 1
                            track_numbers[track_view] = track_font.render(f'{track_view}', False, "#555555")
                            samples[track_view]["window"] = True

            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                if start_button_press:
                    if not audio_start:
                        audio_start = True
                        step = 1
                        light_x_pos = 65
                    else:
                        audio_start = False
                        step = 1
                        light_step = 1
                        light_x_pos = -10
                        pg.mixer.stop()

                    start_button_press = False

        if audio_start:
            play()

        # Render loop
        window_surface.fill("#555555")
        pg.draw.circle(window_surface, color="white",
                       center=(light_x_pos, 50),
                       radius=7,
                       width=0)

        # Draw start button
        if not start_button_press:
            pg.draw.rect(surface=window_surface,
                         color="white",
                         rect=(900, 550, 70, 30),
                         width=0)
            window_surface.blit(start_text, (915, 553))
        else:
            pg.draw.rect(surface=window_surface,
                         color="white",
                         rect=(900, 552, 70, 30),
                         width=0)
            window_surface.blit(start_text, (915, 555))

        # Record button
        record_button = pg.draw.rect(surface=window_surface,
                                     color="white",
                                     rect=(900, 35, 70, 30),
                                     width=0)
        window_surface.blit(record_text, (902, 38))

        # Sample select button
        sample_select = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        }
        sample_y = 100
        for sample in range(8):
            sample_select[sample + 1] = pg.draw.rect(surface=window_surface,
                                                     color="white",
                                                     rect=(900, sample_y, 70, 30),
                                                     width=1)
            window_surface.blit(text_surface, (907, sample_y + 4))
            sample_y += 50

        # Draw pads

        rows = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }

        pad_x_pos = 100
        for pad in range(16):
            if step > 49:
                pad += 48
            elif step > 33:
                pad += 32
            elif step > 17:
                pad += 16
            else:
                pass
            pad_y_pos = 100
            for row in range(8):
                if samples[track_view][row + 1]["steps"][pad + 1][0]:
                    rows[row + 1].append(pg.draw.rect(surface=window_surface,
                                                      color="white",
                                                      rect=(pad_x_pos, pad_y_pos, 30, 30),
                                                      width=0))
                else:
                    rows[row + 1].append(pg.draw.rect(surface=window_surface,
                                                      color="white",
                                                      rect=(pad_x_pos, pad_y_pos, 30, 30),
                                                      width=1))
                pad_y_pos += 50
            pad_x_pos += 50

        # Draw volume button
        sample_volume = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }
        volume_button_y = 100
        y_line = 25
        if volume_adjust:
            volume_text = volume_font.render('Volume', False, "white")
        else:
            volume_text = volume_font.render('Pitch', False, "white")
        window_surface.blit(volume_text, (30, 70))
        volume_pitch_button = pg.draw.rect(surface=window_surface,
                                           color="white",
                                           rect=(25, 69, 60, 20),
                                           width=1)
        for button in range(8):

            sample_volume[button + 1].append(pg.draw.rect(surface=window_surface,
                                                          color="white",
                                                          rect=(25, volume_button_y, 60, 14),
                                                          width=1))

            window_surface.blit(up_text, (30, volume_button_y))

            sample_volume[button + 1].append(pg.draw.rect(surface=window_surface,
                                                          color="white",
                                                          rect=(25, volume_button_y + 15, 60, 14),
                                                          width=1))

            window_surface.blit(down_text, (50, volume_button_y + 15))

            y_line += 50
            volume_button_y += 50

        # Draw step tracker
        circle_x_pos = 115
        circles = []
        for circle in range(16):
            circles.append(pg.draw.circle(window_surface, color="white", center=(circle_x_pos, 50), radius=10, width=1))
            circle_x_pos += 50

        # Draw bpm
        bpm_buttons = [pg.draw.rect(surface=window_surface,
                                    color="white",
                                    rect=(25, 500, 15, 15),
                                    width=0), pg.draw.rect(surface=window_surface,
                                                           color="white",
                                                           rect=(25, 520, 15, 15),
                                                           width=0)]

        window_surface.blit(bpm_text, (45, 500))

        # Measure text and buttons
        measure_buttons = [pg.draw.rect(surface=window_surface,
                                    color="white",
                                    rect=(25, 550, 15, 15),
                                    width=0), pg.draw.rect(surface=window_surface,
                                                           color="white",
                                                           rect=(25, 570, 15, 15),
                                                           width=0)]
        if step > 49:
            measure_number = 4
            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
        elif step > 33:
            measure_number = 3
            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
        elif step > 17:
            measure_number = 2
            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
        else:
            measure_number = 1
            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")

        window_surface.blit(measure_text, (45, 550))

        # Step count
        step_buttons = [pg.draw.rect(surface=window_surface,
                                        color="white",
                                        rect=(230, 550, 15, 15),
                                        width=0), pg.draw.rect(surface=window_surface,
                                                               color="white",
                                                               rect=(230, 570, 15, 15),
                                                               width=0)]

        window_surface.blit(step_text, (250, 550))

        # Tracks
        track_select = []
        track_x = 583
        for button in range(8):
            if samples[button + 1]["window"]:
                track_select.append(pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(track_x, 552, 30, 30),
                                                 width=0))
            else:
                track_select.append(pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(track_x, 552, 30, 30),
                                                 width=1))
            window_surface.blit(track_numbers[button + 1], (track_x + 6, 550))
            track_x += 33
        window_surface.blit(track_text, (500, 550))
        pg.display.flip()
        # pygame_clock.tick(120)
    elif samples[track_view]["mode"] == "instrument":
        for event in pg.event.get():
            if event.type == pg.QUIT:

                is_running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # Start button press
                if 900 < pg.mouse.get_pos()[0] < 970:
                    if 550 < pg.mouse.get_pos()[1] < 580:
                        start_button_press = True

                # Record button press
                if record_button.x < pg.mouse.get_pos()[0] < (record_button.x + 70):
                    if record_button.y < pg.mouse.get_pos()[1] < (record_button.y + 30):
                        recording = True

                # Volume or pitch
                if volume_pitch_button.x < pg.mouse.get_pos()[0] < (volume_pitch_button.x + 70):
                    if volume_pitch_button.y < pg.mouse.get_pos()[1] < (volume_pitch_button.y + 20):
                        if volume_adjust:
                            volume_adjust = False
                        else:
                            volume_adjust = True

                # Pad press
                for row in range(len(rows)):
                    for pad in range(len(rows[1])):
                        if rows[row + 1][pad].x < pg.mouse.get_pos()[0] < (rows[row + 1][pad].x + 30):
                            if rows[row + 1][pad].y < pg.mouse.get_pos()[1] < (rows[row + 1][pad].y + 30):
                                mouse_hold = True
                                row_click = row+1
                                pad_hover_x = rows[row + 1][pad].x
                                original_x = pad_hover_x
                                if step > 47:
                                    pad += 48
                                elif step > 31:
                                    pad += 32
                                elif step > 15:
                                    pad += 16
                                else:
                                    pass
                                pad_hover = pad + 1
                                original_pad = pad_hover

                                if samples[track_view][row + 1]["steps"][pad + 1][0]:

                                    for x in range(pad+1, (samples[track_view][row + 1]["steps"][pad + 1][2] + 1)):
                                        samples[track_view][row + 1]["steps"][x][0] = False
                                        samples[track_view][row + 1]["steps"][x][1] = False
                                        samples[track_view][row + 1]["steps"][x][2] = 0



                                else:
                                    samples[track_view][row + 1]["steps"][pad + 1][0] = True
                                    samples[track_view][row + 1]["steps"][pad + 1][2] = 1

                                    try:
                                        samples[track_view][row + 1]["sample"].play()
                                    except AttributeError:
                                        pass

                    # Sample select press
                    if sample_select[row + 1].x < pg.mouse.get_pos()[0] < (sample_select[row + 1].x + 70):
                        if sample_select[row + 1].y < pg.mouse.get_pos()[1] < (sample_select[row + 1].y + 30):
                            try:
                                sample = askopenfilename()

                                try:
                                    samples[track_view][row + 1]["sample"].fadeout(500)
                                except AttributeError:
                                    pass

                                for f in temp_files:
                                    if f == f"temp-samples\\track {track_view} row {row + 1}.wav":
                                        os.remove(f)
                                samples[track_view][row + 1]["path"] = sample
                                samples[track_view][row + 1]["sample"] = pg.mixer.Sound(sample)
                                samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])

                            except FileNotFoundError:
                                pass

                    # Volume/pitch adjust

                    if sample_volume[row + 1][0].x < pg.mouse.get_pos()[0] < (sample_volume[row + 1][0].x + 60):
                        if sample_volume[row + 1][0].y < pg.mouse.get_pos()[1] < (sample_volume[row + 1][0].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][row + 1]["volume"] == 1.0:
                                        pass
                                    else:
                                        samples[track_view][row + 1]["volume"] = samples[track_view][row + 1]["volume"] + .1
                                        samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])
                                else:
                                    try:
                                        path = f"temp-samples/track {track_view} row {row + 1}.wav"
                                        audio = AudioSegment.from_file(path)

                                    except FileNotFoundError:
                                        samples[track_view][row + 1]["pitch"] += 1
                                        path = samples[track_view][row+1]["path"]
                                        audio = AudioSegment.from_file(path)
                                    fast_sound = speed_change(sound=audio, speed=note_half_step_up)

                                    fast_sound.export(f"temp-samples/track {track_view} row {row+1}.wav", format="wav")
                                    samples[track_view][row + 1]["sample"] = pg.mixer.Sound(f"temp-samples/track {track_view} row {row+1}.wav")
                                    samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])
                            except AttributeError:
                                pass
                    if sample_volume[row + 1][1].x < pg.mouse.get_pos()[0] < (sample_volume[row + 1][1].x + 60):
                        if sample_volume[row + 1][1].y < pg.mouse.get_pos()[1] < (sample_volume[row + 1][1].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][row + 1]["volume"] == 0:
                                        pass
                                    else:
                                        samples[track_view][row + 1]["volume"] = samples[track_view][row + 1]["volume"] - .1
                                        samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])
                                else:
                                    try:
                                        path = f"temp-samples/track {track_view} row {row + 1}.wav"
                                        audio = AudioSegment.from_file(path)

                                    except FileNotFoundError:
                                        samples[track_view][row + 1]["pitch"] += 1
                                        path = samples[track_view][row+1]["path"]
                                        audio = AudioSegment.from_file(path)

                                    slow_sound = speed_change(sound=audio, speed=note_half_step_down)
                                    slow_sound.export(f"temp-samples/track {track_view} row {row+1}.wav", format="wav")
                                    samples[track_view][row + 1]["sample"] = pg.mixer.Sound(f"temp-samples/track {track_view} row {row + 1}.wav")
                                    samples[track_view][row + 1]["sample"].set_volume(samples[track_view][row + 1]["volume"])
                            except AttributeError:
                                pass

                # Bpm adjust
                if bpm_buttons[0].x < pg.mouse.get_pos()[0] < (bpm_buttons[0].x + 15):
                    if bpm_buttons[0].y < pg.mouse.get_pos()[1] < (bpm_buttons[0].y + 15):
                        bpm += 1
                        step_length = (60 / bpm) / 4
                        clock.step_length = step_length
                        bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
                if bpm_buttons[1].x < pg.mouse.get_pos()[0] < (bpm_buttons[1].x + 15):
                    if bpm_buttons[1].y < pg.mouse.get_pos()[1] < (bpm_buttons[1].y + 15):
                        bpm -= 1
                        step_length = (60 / bpm) / 4
                        clock.step_length = step_length
                        bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")

                # Measure select
                if measure_buttons[0].x < pg.mouse.get_pos()[0] < (measure_buttons[0].x + 15):
                    if measure_buttons[0].y < pg.mouse.get_pos()[1] < (measure_buttons[0].y + 15):
                        # step += 16
                        if step < 49:
                            if step <= step_total:
                                step += 17

                        else:
                            pass

                if measure_buttons[1].x < pg.mouse.get_pos()[0] < (measure_buttons[1].x + 15):
                    if measure_buttons[1].y < pg.mouse.get_pos()[1] < (measure_buttons[1].y + 15):
                        if step > 16:
                            step -= 16
                        else:
                            pass

                # Step adjust
                if step_buttons[0].x < pg.mouse.get_pos()[0] < (step_buttons[0].x + 15):
                    if step_buttons[0].y < pg.mouse.get_pos()[1] < (step_buttons[0].y + 15):
                        if step_total == 64:
                            pass
                        else:
                            step_total += 16
                            measure_total += 1
                            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                            step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                            # step = 1

                if step_buttons[1].x < pg.mouse.get_pos()[0] < (step_buttons[1].x + 15):
                    if step_buttons[1].y < pg.mouse.get_pos()[1] < (step_buttons[1].y + 15):
                        if step_total == 16:
                            pass
                        else:
                            step_total -= 16
                            measure_total -= 1
                            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                            step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                            # step = 1

                # Track select
                for button in range(8):
                    if track_select[button].x < pg.mouse.get_pos()[0] < (track_select[button].x + 30):
                        if track_select[button].y < pg.mouse.get_pos()[1] < (track_select[button].y + 30):
                            track_numbers[track_view] = track_font.render(f'{track_view}', False, "White")
                            samples[track_view]["window"] = False
                            track_view = button + 1
                            track_numbers[track_view] = track_font.render(f'{track_view}', False, "#555555")
                            samples[track_view]["window"] = True

            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                for row in range(len(rows)):
                    for pad in range(len(rows[1])):
                        if rows[row + 1][pad].x < pg.mouse.get_pos()[0] < (rows[row + 1][pad].x + 30):
                            if rows[row + 1][pad].y < pg.mouse.get_pos()[1] < (rows[row + 1][pad].y + 30):
                                if step > 47:
                                    pad += 48
                                elif step > 31:
                                    pad += 32
                                elif step > 15:
                                    pad += 16
                                else:
                                    pass

                                try:
                                    samples[track_view][row + 1]["sample"].stop()
                                except AttributeError:
                                    pass
                if start_button_press:
                    if not audio_start:
                        audio_start = True
                        step = 1
                        light_x_pos = 65
                    else:
                        audio_start = False
                        step = 1
                        light_step = 1
                        light_x_pos = -10
                        pg.mixer.stop()

                    start_button_press = False
                if mouse_hold:
                    mouse_hold = False

        if audio_start:
            play()

        # Note hold
        if mouse_hold:
            if pg.mouse.get_pos()[0] > pad_hover_x:
                samples[track_view][row_click]["steps"][original_pad][2] = pad_hover
                pad_hover_x += 50
                pad_hover += 1
                try:
                    samples[track_view][row_click]["steps"][pad_hover][1] = True

                except KeyError:
                    pass
            try:
                if pg.mouse.get_pos()[0] < original_x:
                    samples[track_view][row_click]["steps"][original_pad][2] = pad_hover
                    pad_hover_x = original_x
                    pad_hover = original_pad
                elif pg.mouse.get_pos()[0] < pad_hover_x:
                    pad_hover_x -= 50
                    samples[track_view][row_click]["steps"][pad_hover][1] = False
                    pad_hover -= 1
            except KeyError:
                pad_hover_x = original_x
                pad_hover = original_pad

        # Render loop
        window_surface.fill("#555555")
        pg.draw.circle(window_surface, color="white",
                       center=(light_x_pos, 50),
                       radius=7,
                       width=0)

        # Draw start button
        if not start_button_press:
            pg.draw.rect(surface=window_surface,
                         color="white",
                         rect=(900, 550, 70, 30),
                         width=0)
            window_surface.blit(start_text, (915, 553))
        else:
            pg.draw.rect(surface=window_surface,
                         color="white",
                         rect=(900, 552, 70, 30),
                         width=0)
            window_surface.blit(start_text, (915, 555))

        # Record button
        record_button = pg.draw.rect(surface=window_surface,
                                     color="white",
                                     rect=(900, 35, 70, 30),
                                     width=0)
        window_surface.blit(record_text, (902, 38))

        # Sample select button
        sample_select = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        }
        sample_y = 100
        for sample in range(8):
            sample_select[sample + 1] = pg.draw.rect(surface=window_surface,
                                                     color="white",
                                                     rect=(900, sample_y, 70, 30),
                                                     width=1)
            window_surface.blit(text_surface, (907, sample_y + 4))
            sample_y += 50

        # Draw pads

        rows = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }

        pad_x_pos = 100
        for pad in range(16):
            if step > 49:
                pad += 48
            elif step > 33:
                pad += 32
            elif step > 17:
                pad += 16
            else:
                pass
            pad_y_pos = 100
            for row in range(8):

                if samples[track_view][row + 1]["steps"][pad + 1][1]:
                    if not samples[track_view][row + 1]["steps"][pad + 1][0]:
                        pg.draw.rect(surface=window_surface,
                                     color="white",
                                     rect=(pad_x_pos - 20, pad_y_pos + 9, 50, 10),
                                     width=0)

                if samples[track_view][row + 1]["steps"][pad + 1][0]:
                    rows[row + 1].append(pg.draw.rect(surface=window_surface,
                                                      color="white",
                                                      rect=(pad_x_pos, pad_y_pos, 30, 30),
                                                      width=0))
                else:
                    rows[row + 1].append(pg.draw.rect(surface=window_surface,
                                                      color="white",
                                                      rect=(pad_x_pos, pad_y_pos, 30, 30),
                                                      width=1))
                pad_y_pos += 50
            pad_x_pos += 50

        # Draw volume button
        sample_volume = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }
        volume_button_y = 100
        y_line = 25
        if volume_adjust:
            volume_text = volume_font.render('Volume', False, "white")
        else:
            volume_text = volume_font.render('Pitch', False, "white")
        window_surface.blit(volume_text, (30, 70))
        volume_pitch_button = pg.draw.rect(surface=window_surface,
                                           color="white",
                                           rect=(25, 69, 60, 20),
                                           width=1)
        for button in range(8):

            sample_volume[button + 1].append(pg.draw.rect(surface=window_surface,
                                                          color="white",
                                                          rect=(25, volume_button_y, 60, 14),
                                                          width=1))

            window_surface.blit(up_text, (30, volume_button_y))

            sample_volume[button + 1].append(pg.draw.rect(surface=window_surface,
                                                          color="white",
                                                          rect=(25, volume_button_y + 15, 60, 14),
                                                          width=1))

            window_surface.blit(down_text, (50, volume_button_y + 15))

            y_line += 50
            volume_button_y += 50

        # Draw step tracker
        circle_x_pos = 115
        circles = []
        for circle in range(16):
            circles.append(pg.draw.circle(window_surface, color="white", center=(circle_x_pos, 50), radius=10, width=1))
            circle_x_pos += 50

        # Draw bpm
        bpm_buttons = [pg.draw.rect(surface=window_surface,
                                    color="white",
                                    rect=(25, 500, 15, 15),
                                    width=0), pg.draw.rect(surface=window_surface,
                                                           color="white",
                                                           rect=(25, 520, 15, 15),
                                                           width=0)]

        window_surface.blit(bpm_text, (45, 500))

        # Measure text and buttons
        measure_buttons = [pg.draw.rect(surface=window_surface,
                                    color="white",
                                    rect=(25, 550, 15, 15),
                                    width=0), pg.draw.rect(surface=window_surface,
                                                           color="white",
                                                           rect=(25, 570, 15, 15),
                                                           width=0)]
        if step > 49:
            measure_number = 4
            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
        elif step > 33:
            measure_number = 3
            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
        elif step > 17:
            measure_number = 2
            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
        else:
            measure_number = 1
            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")

        window_surface.blit(measure_text, (45, 550))

        # Step count
        step_buttons = [pg.draw.rect(surface=window_surface,
                                        color="black",
                                        rect=(230, 550, 15, 15),
                                        width=0), pg.draw.rect(surface=window_surface,
                                                               color="white",
                                                               rect=(230, 570, 15, 15),
                                                               width=0)]

        window_surface.blit(step_text, (250, 550))

        # Tracks
        track_select = []
        track_x = 583
        for button in range(8):
            if samples[button + 1]["window"]:
                track_select.append(pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(track_x, 552, 30, 30),
                                                 width=0))
            else:
                track_select.append(pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(track_x, 552, 30, 30),
                                                 width=1))
            window_surface.blit(track_numbers[button + 1], (track_x + 6, 550))
            track_x += 33
        window_surface.blit(track_text, (500, 550))
        pg.display.flip()












