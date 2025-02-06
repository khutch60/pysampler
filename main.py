from metronome import Clock
from pitch_shift import PitchShift
import pygame as pg
import tkinter
from tkinter.filedialog import askopenfilename
from text import *
from playback import play
from file_handler import Samples, clear_one_sample, clear_all_temp_samples

clear_all_temp_samples()
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
file_load = Samples()
file_load.new()
samples = file_load.samples
samples[0][1]["window"] = True

pg.mixer.set_num_channels(30)

pitch_shift = PitchShift()

step = 1
clock = Clock()

bpm = file_load.params["bpm"]
step_length = ((60/bpm) / 4)
clock.step_length = step_length
audio_start = False

light_step = 1
light_x_pos = -10

step_total = file_load.params["steps"]
measure_number = 1
measure_total = file_load.params["measures"]

start_button_press = False
new_button_press = False

volume_adjust = True
mouse_hold = False
row_click = None
pad_hover = None
original_pad = None
original_x = None
pad_hover_x = None



track_view = 0


bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")

for track in range(8):
    if samples[track][1]["window"]:
        track_view = track
track_numbers[track_view] = track_font.render(f"{track_view + 1}", False, "#555555")


while is_running:

    if samples[track_view][1]["mode"] == "drum":
        mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")
        for event in pg.event.get():
            if event.type == pg.QUIT:

                is_running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                # Start button press
                if 900 < pg.mouse.get_pos()[0] < 970:
                    if 550 < pg.mouse.get_pos()[1] < 580:
                        start_button_press = True


                # Save button press
                if save_button.x < pg.mouse.get_pos()[0] < save_button.x + 30:
                    if save_button.y < pg.mouse.get_pos()[1] < save_button.y + 30:
                        file_load.save()

                # Load button press
                if load_button.x < pg.mouse.get_pos()[0] < load_button.x + 30:
                    if load_button.y < pg.mouse.get_pos()[1] < load_button.y + 30:
                        track_numbers[track_view] = track_font.render(f"{track_view + 1}", False, "white")
                        file_load.load()
                        samples = file_load.samples
                        bpm = file_load.params["bpm"]
                        step_total = file_load.params["steps"]
                        measure_total = file_load.params["measures"]
                        step_length = (60 / bpm) / 4
                        clock.step_length = step_length
                        bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
                        measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                        step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                        mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")
                        track_view = 0
                        track_numbers[track_view] = track_font.render(f"{track_view + 1}", False, "#555555")



                # New button press
                if new_button.x < pg.mouse.get_pos()[0] < (new_button.x + 70):
                    if new_button.y < pg.mouse.get_pos()[1] < (new_button.y + 30):

                        new_button_press = True

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
                                        if samples[track_view][0][row]["steps"][check_start + 1][1]:
                                            samples[track_view][0][row]["steps"][check_start + 1][1] = False
                                            samples[track_view][0][row]["steps"][check_start + 1][2] = 0
                                            check_start += 1
                                elif samples[track_view][0][row]["steps"][pad][1]:
                                    check_start = pad
                                    samples[track_view][0][row]["steps"][check_start][0] = True
                                    for x in range(step_total - pad):
                                        samples[track_view][0][row]["steps"][check_start][1] = False
                                        samples[track_view][0][row]["steps"][check_start][2] = 0
                                        check_start += 1
                                else:
                                    samples[track_view][0][row]["steps"][pad][0] = True
                                    samples[track_view][0][row]["steps"][pad][1] = False
                                    samples[track_view][0][row]["steps"][pad][2] = 1
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
                                samples[track_view][0][row]["path"] = sample
                                samples[track_view][0][row]["sample"] = pg.mixer.Sound(sample)
                                samples[track_view][0][row]["pitch"] = 0
                                samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])
                                clear_one_sample(path=f"temp-samples\\track {track_view} row {row}.wav")




                            except FileNotFoundError:
                                pass

                    # Volume/pitch adjust

                    if sample_volume[row][0].x < pg.mouse.get_pos()[0] < (sample_volume[row][0].x + 60):
                        if sample_volume[row][0].y < pg.mouse.get_pos()[1] < (sample_volume[row][0].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][0][row]["volume"] >= 1.0:
                                        pass
                                    else:
                                        samples[track_view][0][row]["volume"] = samples[track_view][0][row]["volume"] + .1
                                        samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])
                                else:
                                    samples[track_view][0][row]["sample"] = pitch_shift.shift_up(track=track_view,
                                                                                                 sample=row,
                                                                                                 samples=samples)
                                    samples[track_view][0][row]["pitch"] += 1
                            except AttributeError:
                                pass

                    if sample_volume[row][1].x < pg.mouse.get_pos()[0] < (sample_volume[row][1].x + 60):
                        if sample_volume[row][1].y < pg.mouse.get_pos()[1] < (sample_volume[row][1].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][0][row]["volume"] <= 0:
                                        pass
                                    else:
                                        samples[track_view][0][row]["volume"] = samples[track_view][0][row]["volume"] - .1
                                        samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])
                                else:
                                    samples[track_view][0][row]["sample"] = pitch_shift.shift_down(track=track_view,
                                                                                                 sample=row,
                                                                                                 samples=samples)
                                    samples[track_view][0][row]["pitch"] -= 1
                            except AttributeError:
                                pass

                # Bpm adjust
                if bpm_buttons[0].x < pg.mouse.get_pos()[0] < (bpm_buttons[0].x + 15):
                    if bpm_buttons[0].y < pg.mouse.get_pos()[1] < (bpm_buttons[0].y + 15):
                        bpm += 1
                        file_load.params["bpm"] = bpm
                        step_length = (60 / bpm) / 4
                        clock.step_length = step_length
                        bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
                if bpm_buttons[1].x < pg.mouse.get_pos()[0] < (bpm_buttons[1].x + 15):
                    if bpm_buttons[1].y < pg.mouse.get_pos()[1] < (bpm_buttons[1].y + 15):
                        bpm -= 1
                        file_load.params["bpm"] = bpm
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
                            file_load.params["steps"] = step_total
                            measure_total += 1
                            file_load.params["measures"] = measure_total
                            measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                            step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                            # step = 1

                if step_buttons[1].x < pg.mouse.get_pos()[0] < (step_buttons[1].x + 15):
                    if step_buttons[1].y < pg.mouse.get_pos()[1] < (step_buttons[1].y + 15):

                        if step_total == 16:
                            pass
                        else:
                            step_total -= 16
                            file_load.params["steps"] = step_total
                            measure_total -= 1
                            file_load.params["measures"] = measure_total
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

                if new_button_press:
                    file_load.new()
                    samples = file_load.samples

                    track_numbers[track_view] = track_font.render(f"{track_view + 1}", False, "white")
                    track_view = 0
                    samples[0][1]["window"] = True
                    track_numbers[track_view] = track_font.render(f"{track_view + 1}", False, "#555555")

                    bpm = file_load.params["bpm"]
                    step_length = ((60 / bpm) / 4)
                    clock.step_length = step_length
                    audio_start = False

                    light_step = 1
                    light_x_pos = -10

                    step_total = file_load.params["steps"]
                    measure_number = 1
                    measure_total = file_load.params["measures"]



                    new_button_press = False



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

        # Draw save and load buttons
        save_button = pg.draw.rect(surface=window_surface,
                         color="white",
                         rect=(900, 502, 30, 30),
                         width=0)
        window_surface.blit(save_text, (908, 505))

        load_button = pg.draw.rect(surface=window_surface,
                         color="white",
                         rect=(940, 502, 30, 30),
                         width=0)
        window_surface.blit(load_text, (950, 505))


        # New button
        if not new_button_press:
            new_button = pg.draw.rect(surface=window_surface,
                                         color="white",
                                         rect=(900, 35, 70, 30),
                                         width=1)
            window_surface.blit(new_text, (908, 38))
        else:
            new_button = pg.draw.rect(surface=window_surface,
                                      color="white",
                                      rect=(900, 37, 70, 30),
                                      width=1)
            window_surface.blit(new_text, (908, 40))

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

                # Save button press
                if save_button.x < pg.mouse.get_pos()[0] < save_button.x + 30:
                    if save_button.y < pg.mouse.get_pos()[1] < save_button.y + 30:
                        file_load.save()


                # Load button press
                if load_button.x < pg.mouse.get_pos()[0] < load_button.x + 30:
                    if load_button.y < pg.mouse.get_pos()[1] < load_button.y + 30:
                        file_load.load()
                        samples = file_load.samples
                        bpm = file_load.params["bpm"]
                        step_total = file_load.params["steps"]
                        measure_total = file_load.params["measures"]
                        step_length = (60 / bpm) / 4
                        clock.step_length = step_length
                        bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
                        measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                        step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                        mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")
                        track_view = 0


                # New button press
                if new_button.x < pg.mouse.get_pos()[0] < (new_button.x + 70):
                    if new_button.y < pg.mouse.get_pos()[1] < (new_button.y + 30):
                        new_button_press = True

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
                                    samples[track_view][0][row]["steps"][pad][0] = False
                                    for x in range(pad, (samples[track_view][0][row]["steps"][pad][2] + 1)):
                                        samples[track_view][0][row]["steps"][x][0] = False
                                        samples[track_view][0][row]["steps"][x][1] = False
                                        samples[track_view][0][row]["steps"][x][2] = 0
                                        if samples[track_view][0][row]["steps"][x + 1][0]:
                                            break
                                    mouse_hold = False
                                elif samples[track_view][0][row]["steps"][pad][1]:
                                    check_start = pad
                                    samples[track_view][0][row]["steps"][check_start][0] = True
                                    for x in range(step_total - pad):
                                        samples[track_view][0][row]["steps"][check_start][1] = False
                                        samples[track_view][0][row]["steps"][check_start][2] = 0
                                        check_start += 1
                                else:
                                    check_start = pad
                                    samples[track_view][0][row]["steps"][pad][0] = True
                                    samples[track_view][0][row]["steps"][pad][1] = False
                                    samples[track_view][0][row]["steps"][pad][2] = 1
                                    for x in range(step_total - pad + 1):
                                        if samples[track_view][0][row]["steps"][check_start][0]:
                                            break
                                        else:
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

                                samples[track_view][0][row]["path"] = sample
                                samples[track_view][0][row]["sample"] = pg.mixer.Sound(sample)
                                samples[track_view][0][row]["pitch"] = 0
                                samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])
                                clear_one_sample(path=f"temp-samples\\track {track_view} row {row}.wav")

                            except FileNotFoundError:
                                pass

                    # Volume/pitch adjust

                    if sample_volume[row][0].x < pg.mouse.get_pos()[0] < (sample_volume[row][0].x + 60):
                        if sample_volume[row][0].y < pg.mouse.get_pos()[1] < (sample_volume[row][0].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][0][row]["volume"] >= 1.0:
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
                                    samples[track_view][0][row]["pitch"] += 1
                            except AttributeError:
                                pass

                    if sample_volume[row][1].x < pg.mouse.get_pos()[0] < (sample_volume[row][1].x + 60):
                        if sample_volume[row][1].y < pg.mouse.get_pos()[1] < (sample_volume[row][1].y + 14):
                            try:
                                if volume_adjust:
                                    if samples[track_view][0][row]["volume"] <= 0:
                                        pass
                                    else:
                                        samples[track_view][0][row]["volume"] = samples[track_view][0][row]["volume"] - .1
                                        samples[track_view][0][row]["sample"].set_volume(samples[track_view][0][row]["volume"])
                                else:
                                    samples[track_view][0][row]["sample"] = pitch_shift.shift_down(track=track_view,
                                                                                                   sample=row,
                                                                                                   samples=samples)
                                    samples[track_view][0][row]["pitch"] -= 1
                            except AttributeError:
                                pass

                # Bpm adjust
                if bpm_buttons[0].x < pg.mouse.get_pos()[0] < (bpm_buttons[0].x + 15):
                    if bpm_buttons[0].y < pg.mouse.get_pos()[1] < (bpm_buttons[0].y + 15):
                        bpm += 1
                        file_load.params["bpm"] = bpm
                        step_length = (60 / bpm) / 4
                        clock.step_length = step_length
                        bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
                if bpm_buttons[1].x < pg.mouse.get_pos()[0] < (bpm_buttons[1].x + 15):
                    if bpm_buttons[1].y < pg.mouse.get_pos()[1] < (bpm_buttons[1].y + 15):
                        bpm -= 1
                        file_load.params["bpm"] = bpm
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
                            file_load.params["steps"] = step_total
                            measure_total += 1
                            file_load.params["measures"] = measure_total
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
                            file_load.params["steps"] = step_total
                            measure_total -= 1
                            file_load.params["measures"] = measure_total
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
                if new_button_press:
                    file_load.new()
                    samples = file_load.samples

                    track_numbers[track_view] = track_font.render(f"{track_view + 1}", False, "white")
                    track_view = 0
                    samples[0][1]["window"] = True
                    track_numbers[track_view] = track_font.render(f"{track_view + 1}", False, "#555555")

                    bpm = file_load.params["bpm"]
                    step_length = ((60 / bpm) / 4)
                    clock.step_length = step_length
                    audio_start = False

                    light_step = 1
                    light_x_pos = -10

                    step_total = file_load.params["steps"]
                    measure_number = 1
                    measure_total = file_load.params["measures"]

                    bpm_text = bpm_font.render(f"{bpm} bpm", False, "white")
                    measure_text = measure_font.render(f"Measure: {measure_number}/{measure_total}", False, "white")
                    step_text = measure_font.render(f"Step Count: {step_total}", False, "white")
                    mode_text = mode_font.render(f"Mode: {samples[track_view][1]['mode'].title()}", False, "white")

                    new_button_press = False

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
                if samples[track_view][0][row_click]["steps"][pad_hover + 1][0]:
                    mouse_hold = False

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

        # Draw save and load buttons
        save_button = pg.draw.rect(surface=window_surface,
                                   color="white",
                                   rect=(900, 502, 30, 30),
                                   width=0)
        window_surface.blit(save_text, (908, 505))

        load_button = pg.draw.rect(surface=window_surface,
                                   color="white",
                                   rect=(940, 502, 30, 30),
                                   width=0)
        window_surface.blit(load_text, (950, 505))

        # New button
        if not new_button_press:
            new_button = pg.draw.rect(surface=window_surface,
                                      color="white",
                                      rect=(900, 35, 70, 30),
                                      width=1)
            window_surface.blit(new_text, (908, 38))
        else:
            new_button = pg.draw.rect(surface=window_surface,
                                      color="white",
                                      rect=(900, 37, 70, 30),
                                      width=1)
            window_surface.blit(new_text, (908, 40))

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












