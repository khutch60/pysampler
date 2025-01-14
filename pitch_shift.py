from pydub import AudioSegment
import pygame as pg

class PitchShift:
    def __init__(self):
        self.note_up = 1.05946
        self.note_down = 0.94054

    def speed_change(self, sound, speed):
        sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
            "frame_rate": int(sound.frame_rate * speed)
        })
        return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

    def shift_up(self, track, sample, samples):
        try:
            path = f"temp-samples/track {track} row {sample}.wav"
            audio = AudioSegment.from_file(path)
        except FileNotFoundError:
            path = samples[track][0][sample]["path"]
            audio = AudioSegment.from_file(path)
        slow_sound = self.speed_change(sound=audio, speed=self.note_up)
        slow_sound.export(f"temp-samples/track {track} row {sample}.wav", format="wav")
        new_sound = pg.mixer.Sound(f"temp-samples/track {track} row {sample}.wav")
        new_sound.set_volume(samples[track][0][sample]["volume"])
        return new_sound

    def shift_down(self, track, sample, samples):
        try:
            path = f"temp-samples/track {track} row {sample}.wav"
            audio = AudioSegment.from_file(path)
        except FileNotFoundError:
            path = samples[track][0][sample]["path"]
            audio = AudioSegment.from_file(path)
        slow_sound = self.speed_change(sound=audio, speed=self.note_down)
        slow_sound.export(f"temp-samples/track {track} row {sample}.wav", format="wav")
        new_sound = pg.mixer.Sound(f"temp-samples/track {track} row {sample}.wav")
        new_sound.set_volume(samples[track][0][sample]["volume"])
        return new_sound