from metronome import Clock
from pitch_shift import PitchShift
import os
import glob
import pygame as pg
import tkinter
from tkinter.filedialog import askopenfilename
from text import *
from playback import play


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
samples = {}

for x in range(8):
    samples[x] = [[{"sample": None,
        "path": None,
        "steps": [[False, False, 0] for x in range(64)],
        "volume": 0.5,
        "pitch": 0} for y in range(8)],
         {"window": False, "mode": "drum"}]


samples[0][1]["window"] = True

samples[0][0][0]["sample"] = pg.mixer.Sound("samples/synthwave-kick-punch_C_minor.wav")
samples[0][0][0]["path"] = "samples/synthwave-kick-punch_C_minor.wav"
samples[0][0][0]["pitch"] = -2
samples[0][0][0]["steps"][3][0] = True

samples[0][0][1]["sample"] = pg.mixer.Sound("samples/origin-snare.wav")
samples[0][0][1]["path"] = "samples/origin-snare.wav"
samples[0][0][1]["pitch"] = -2

pg.mixer.set_num_channels(30)

pitch_shift = PitchShift()

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

track_view = 0


bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")




for track in range(8):
    if samples[track][1]["window"]:
        track_view = track
track_numbers[track_view] = track_font.render(f"{track_view + 1}", False, "#555555")


#set project parameters
for track in samples:
    for sample in range(8):
        try:
            samples[track][0][sample]["sample"].set_volume(samples[track][0][sample]["volume"])
        except AttributeError:
            pass
        if samples[track][0][sample]["pitch"] > 0:
            for x in range(samples[track][0][sample]["pitch"]):
                samples[track][0][sample]["sample"] = pitch_shift.shift_up(track=track, sample=sample, samples=samples)

        elif samples[track][0][sample]["pitch"] < 0:
            for x in range(samples[track][0][sample]["pitch"] * -1):
                samples[track][0][sample]["sample"] = pitch_shift.shift_down(track=track, sample=sample, samples=samples)




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

    elif samples[track_view][1]["mode"] == "drum":
        mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")
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
                        if rows[row][pad].x < pg.mouse.get_pos()[0] < (rows[row][pad].x + 30):
                            if rows[row][pad].y < pg.mouse.get_pos()[1] < (rows[row][pad].y + 30):
                                if step > 47:
                                    pad += 48
                                elif step > 31:
                                    pad += 32
                                elif step > 15:
                                    pad += 16
                                else:
                                    pass
                                if samples[track_view][0][row]["steps"][pad][0]:
                                    check_start = pad
                                    samples[track_view][0][row]["steps"][pad][0] = False
                                    samples[track_view][0][row]["steps"][pad][1] = False
                                    samples[track_view][0][row]["steps"][pad][2] = 0
                                    for x in range(step_total - pad):
                                        if samples[track_view][0][row]["steps"][check_start][0]:
                                            break
                                        elif samples[track_view][0][row]["steps"][check_start][1]:
                                            samples[track_view][0][row]["steps"][check_start][1] = False
                                            samples[track_view][0][row]["steps"][check_start][2] = 0
                                            check_start += 1
                                else:
                                    samples[track_view][0][row]["steps"][pad][0] = True
                                    try:
                                        samples[track_view][0][row]["sample"].play()
                                    except AttributeError:
                                        pass

                    # Sample select press

                    if sample_select[row].x < pg.mouse.get_pos()[0] < (sample_select[row].x + 70):
                        if sample_select[row].y < pg.mouse.get_pos()[1] < (sample_select[row].y + 30):
                            try:
                                sample = askopenfilename()

                                try:
                                    samples[track_view][0][row]["sample"].fadeout(500)
                                except AttributeError:
                                    pass

                                for f in temp_files:
                                    if f == f"temp-samples\\track {track_view} row {row + 1}.wav":
                                        os.remove(f)
                                samples[track_view][0][row]["path"] = sample
                                samples[track_view][0][row]["sample"] = pg.mixer.Sound(sample)
                                samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])

                            except FileNotFoundError:
                                pass

                    # Volume/pitch adjust

                    if sample_volume[row][0].x < pg.mouse.get_pos()[0] < (sample_volume[row][0].x + 60):
                        if sample_volume[row][0].y < pg.mouse.get_pos()[1] < (sample_volume[row][0].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][0][row]["volume"] == 1.0:
                                        pass
                                    else:
                                        samples[track_view][0][row]["volume"] = samples[track_view][0][row]["volume"] + .1
                                        samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])
                                else:
                                    samples[track_view][0][row]["sample"] = pitch_shift.shift_up(track=track_view,
                                                                                                 sample=row,
                                                                                                 samples=samples)
                            except AttributeError:
                                pass

                    if sample_volume[row][1].x < pg.mouse.get_pos()[0] < (sample_volume[row][1].x + 60):
                        if sample_volume[row][1].y < pg.mouse.get_pos()[1] < (sample_volume[row][1].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][0][row]["volume"] == 0:
                                        pass
                                    else:
                                        samples[track_view][0][row]["volume"] = samples[track_view][0][row]["volume"] - .1
                                        samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])
                                else:
                                    samples[track_view][0][row]["sample"] = pitch_shift.shift_down(track=track_view,
                                                                                                 sample=row,
                                                                                                 samples=samples)
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
                            if measure_number == measure_total:
                                pass
                            elif step <= step_total:
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
                            if measure_total < measure_number:
                                measure_number = measure_total
                                step -= 16

                        measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False,"white")
                        step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                            # step = 1

                # Track select
                for button in range(8):
                    if track_select[button].x < pg.mouse.get_pos()[0] < (track_select[button].x + 30):
                        if track_select[button].y < pg.mouse.get_pos()[1] < (track_select[button].y + 30):
                            track_numbers[track_view] = track_font.render(f'{track_view + 1}', False, "White")
                            samples[track_view][1]["window"] = False
                            track_view = button
                            track_numbers[track_view] = track_font.render(f'{track_view + 1}', False, "#555555")
                            samples[track_view][1]["window"] = True

                # Mode select
                if mode_select.x < pg.mouse.get_pos()[0] < (mode_select.x + 80):
                    if mode_select.y < pg.mouse.get_pos()[1] < (mode_select.y + 30):
                        samples[track_view][1]["mode"] = "instrument"
                        mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")

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
            if clock.step():
                if light_step > 16:
                    light_step = 1
                    light_x_pos = 65
                play(sample_dict=samples, step_num=step)
                step += 1
                light_step += 1
                light_x_pos += 50
                if step > step_total:
                    step = 1



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
        sample_select = [None, None, None, None, None, None, None, None]

        sample_y = 100
        for sample in range(8):
            sample_select[sample] = pg.draw.rect(surface=window_surface,
                                                     color="white",
                                                     rect=(900, sample_y, 70, 30),
                                                     width=1)
            window_surface.blit(text_surface, (907, sample_y + 4))
            sample_y += 50

        # Draw pads

        rows = [[], [], [], [], [], [], [], []]


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
                if samples[track_view][0][row]["steps"][pad][0]:
                    rows[row].append(pg.draw.rect(surface=window_surface,
                                                      color="white",
                                                      rect=(pad_x_pos, pad_y_pos, 30, 30),
                                                      width=0))
                else:
                    rows[row].append(pg.draw.rect(surface=window_surface,
                                                      color="white",
                                                      rect=(pad_x_pos, pad_y_pos, 30, 30),
                                                      width=1))
                pad_y_pos += 50
            pad_x_pos += 50

        # Draw volume button
        sample_volume = [[], [], [], [], [], [], [], []]

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

            sample_volume[button].append(pg.draw.rect(surface=window_surface,
                                                          color="white",
                                                          rect=(25, volume_button_y, 60, 14),
                                                          width=1))

            window_surface.blit(up_text, (30, volume_button_y))

            sample_volume[button].append(pg.draw.rect(surface=window_surface,
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
            if samples[button][1]["window"]:
                track_select.append(pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(track_x, 552, 30, 30),
                                                 width=0))
            else:
                track_select.append(pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(track_x, 552, 30, 30),
                                                 width=1))
            window_surface.blit(track_numbers[button], (track_x + 6, 550))
            track_x += 33
        window_surface.blit(track_text, (500, 550))


        mode_select = pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(497, 502, 80, 30),
                                                 width=1)
        window_surface.blit(mode_text, (500, 500))

        pg.display.flip()

    elif samples[track_view][1]["mode"] == "instrument":
        mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")
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
                        if rows[row][pad].x < pg.mouse.get_pos()[0] < (rows[row][pad].x + 30):
                            if rows[row][pad].y < pg.mouse.get_pos()[1] < (rows[row][pad].y + 30):
                                mouse_hold = True
                                row_click = row
                                pad_hover_x = rows[row][pad].x
                                original_x = pad_hover_x
                                if step > 47:
                                    pad += 48
                                elif step > 31:
                                    pad += 32
                                elif step > 15:
                                    pad += 16
                                else:
                                    pass
                                pad_hover = pad
                                original_pad = pad_hover

                                if samples[track_view][0][row]["steps"][pad][0]:
                                    for x in range(pad, (samples[track_view][0][row]["steps"][pad][2] + 1)):
                                        mouse_hold = False
                                        samples[track_view][0][row]["steps"][x][0] = False
                                        samples[track_view][0][row]["steps"][x][1] = False
                                        samples[track_view][0][row]["steps"][x][2] = 0
                                else:
                                    check_start = pad
                                    samples[track_view][0][row]["steps"][pad][0] = True
                                    samples[track_view][0][row]["steps"][pad][1] = False
                                    samples[track_view][0][row]["steps"][pad][2] = 1
                                    for x in range(step_total - pad):
                                        if samples[track_view][0][row]["steps"][check_start][0]:
                                            break
                                        elif samples[track_view][0][row]["steps"][check_start][1]:
                                            samples[track_view][0][row]["steps"][check_start][1] = False
                                            samples[track_view][0][row]["steps"][check_start][2] = 0
                                            check_start += 1

                                    try:
                                        samples[track_view][0][row]["sample"].play()
                                    except AttributeError:
                                        pass

                    # Sample select press
                    if sample_select[row].x < pg.mouse.get_pos()[0] < (sample_select[row].x + 70):
                        if sample_select[row].y < pg.mouse.get_pos()[1] < (sample_select[row].y + 30):
                            try:
                                sample = askopenfilename()

                                try:
                                    samples[track_view][0][row]["sample"].fadeout(500)
                                except AttributeError:
                                    pass

                                for f in temp_files:
                                    if f == f"temp-samples\\track {track_view} row {row + 1}.wav":
                                        os.remove(f)
                                samples[track_view][0][row]["path"] = sample
                                samples[track_view][0][row]["sample"] = pg.mixer.Sound(sample)
                                samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])

                            except FileNotFoundError:
                                pass

                    # Volume/pitch adjust

                    if sample_volume[row][0].x < pg.mouse.get_pos()[0] < (sample_volume[row][0].x + 60):
                        if sample_volume[row][0].y < pg.mouse.get_pos()[1] < (sample_volume[row][0].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][0][row]["volume"] == 1.0:
                                        pass
                                    else:
                                        samples[track_view][0][row]["volume"] = samples[track_view][0][row][
                                                                                    "volume"] + .1
                                        samples[track_view][0][row]["sample"].set_volume(
                                            samples[track_view][0][row]["volume"])
                                else:
                                    samples[track_view][0][row]["sample"] = pitch_shift.shift_up(track=track_view,
                                                                                                 sample=row,
                                                                                                 samples=samples)
                            except AttributeError:
                                pass

                    if sample_volume[row][1].x < pg.mouse.get_pos()[0] < (sample_volume[row][1].x + 60):
                        if sample_volume[row][1].y < pg.mouse.get_pos()[1] < (sample_volume[row][1].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][0][row]["volume"] == 0:
                                        pass
                                    else:
                                        samples[track_view][0][row]["volume"] = samples[track_view][0][row]["volume"] - .1
                                        samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])
                                else:
                                    samples[track_view][0][row]["sample"] = pitch_shift.shift_down(track=track_view,
                                                                                                   sample=row,
                                                                                                   samples=samples)
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
                            if measure_number == measure_total:
                                pass
                            elif step <= step_total:
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
                            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False,
                                                               "white")
                            step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                            # step = 1

                if step_buttons[1].x < pg.mouse.get_pos()[0] < (step_buttons[1].x + 15):
                    if step_buttons[1].y < pg.mouse.get_pos()[1] < (step_buttons[1].y + 15):

                        if step_total == 16:
                            pass
                        else:
                            step_total -= 16
                            measure_total -= 1
                            if measure_total < measure_number:
                                measure_number = measure_total
                                step -= 16

                        measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                        step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                        # step = 1

                # Track select
                for button in range(8):
                    if track_select[button].x < pg.mouse.get_pos()[0] < (track_select[button].x + 30):
                        if track_select[button].y < pg.mouse.get_pos()[1] < (track_select[button].y + 30):
                            track_numbers[track_view] = track_font.render(f'{track_view + 1}', False, "White")
                            samples[track_view][1]["window"] = False
                            track_view = button
                            track_numbers[track_view] = track_font.render(f'{track_view + 1}', False, "#555555")
                            samples[track_view][1]["window"] = True

                # Mode select
                if mode_select.x < pg.mouse.get_pos()[0] < (mode_select.x + 80):
                    if mode_select.y < pg.mouse.get_pos()[1] < (mode_select.y + 30):
                        samples[track_view][1]["mode"] = "drum"

                        mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")


            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                for row in range(len(rows)):
                    for pad in range(len(rows[1])):
                        if rows[row][pad].x < pg.mouse.get_pos()[0] < (rows[row][pad].x + 30):
                            if rows[row][pad].y < pg.mouse.get_pos()[1] < (rows[row][pad].y + 30):
                                if step > 47:
                                    pad += 48
                                elif step > 31:
                                    pad += 32
                                elif step > 15:
                                    pad += 16
                                else:
                                    pass

                                try:
                                    samples[track_view][0][row]["sample"].stop()
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
            if clock.step():
                if light_step > 16:
                    light_step = 1
                    light_x_pos = 65
                play(sample_dict=samples, step_num=step)
                step += 1
                light_step += 1
                light_x_pos += 50
                if step > step_total:
                    step = 1

        # Note hold
        if mouse_hold:
            if pg.mouse.get_pos()[0] > pad_hover_x:
                samples[track_view][0][row_click]["steps"][original_pad][2] = pad_hover
                if pad_hover_x == 850:
                    pass
                else:
                    pad_hover_x += 50
                    pad_hover += 1
                try:
                    samples[track_view][0][row_click]["steps"][pad_hover][1] = True
                except KeyError:
                    pass
            try:
                if pg.mouse.get_pos()[0] < original_x:
                    samples[track_view][0][row_click]["steps"][original_pad][2] = pad_hover
                    pad_hover_x = original_x
                    pad_hover = original_pad
                elif pg.mouse.get_pos()[0] < pad_hover_x:
                    pad_hover_x -= 50
                    samples[track_view][0][row_click]["steps"][pad_hover][1] = False
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
        sample_select = [None, None, None, None, None, None, None, None]
        sample_y = 100
        for sample in range(8):
            sample_select[sample] = pg.draw.rect(surface=window_surface,
                                                     color="white",
                                                     rect=(900, sample_y, 70, 30),
                                                     width=1)
            window_surface.blit(text_surface, (907, sample_y + 4))
            sample_y += 50

        # Draw pads

        rows = [[], [], [], [], [], [], [], []]

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
                if samples[track_view][0][row]["steps"][pad][1]:
                    if not samples[track_view][0][row]["steps"][pad][0]:
                        pg.draw.rect(surface=window_surface,
                                     color="white",
                                     rect=(pad_x_pos - 20, pad_y_pos + 9, 50, 10),
                                     width=0)

                if samples[track_view][0][row]["steps"][pad][0]:
                    rows[row].append(pg.draw.rect(surface=window_surface,
                                                      color="white",
                                                      rect=(pad_x_pos, pad_y_pos, 30, 30),
                                                      width=0))
                else:
                    rows[row].append(pg.draw.rect(surface=window_surface,
                                                      color="white",
                                                      rect=(pad_x_pos, pad_y_pos, 30, 30),
                                                      width=1))
                pad_y_pos += 50
            pad_x_pos += 50

        # Draw volume button
        sample_volume = [[], [], [], [], [], [], [], []]
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

            sample_volume[button].append(pg.draw.rect(surface=window_surface,
                                                          color="white",
                                                          rect=(25, volume_button_y, 60, 14),
                                                          width=1))

            window_surface.blit(up_text, (30, volume_button_y))

            sample_volume[button].append(pg.draw.rect(surface=window_surface,
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
            if samples[button][1]["window"]:
                track_select.append(pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(track_x, 552, 30, 30),
                                                 width=0))
            else:
                track_select.append(pg.draw.rect(surface=window_surface,
                                                 color="white",
                                                 rect=(track_x, 552, 30, 30),
                                                 width=1))
            window_surface.blit(track_numbers[button], (track_x + 6, 550))
            track_x += 33

        mode_select = pg.draw.rect(surface=window_surface,
                                   color="white",
                                   rect=(497, 502, 80, 30),
                                   width=1)
        window_surface.blit(mode_text, (500, 500))

        window_surface.blit(track_text, (500, 550))
        pg.display.flip()












