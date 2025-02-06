import pygame as pg

pg.font.init()

start_font = pg.font.SysFont('Arial', 20)
start_text = start_font.render("Play", False, "#555555")

new_font = pg.font.SysFont('Arial', 20)
new_text = new_font.render("Reset", False, "white")

back_font = pg.font.SysFont('Arial', 20)
back_text = back_font.render("Back", False, "#555555")

select_font = pg.font.SysFont('Arial', 20)
text_surface = select_font.render('Select', False, "white")

up_down_font = pg.font.SysFont('Arial', 10)
up_text = up_down_font.render('Up', False, "white")
down_text = up_down_font.render('Down', False, "white")

volume_font = pg.font.SysFont('Arial', 15)
volume_text = volume_font.render('Volume', False, "white")

save_load_font = pg.font.SysFont('Arial', 20)
save_text = save_load_font.render('S', False, "#555555")
load_text = save_load_font.render('L', False, "#555555")

bpm_font = pg.font.SysFont('Arial', 30)


measure_font = pg.font.SysFont('Arial', 30)


step_font = pg.font.SysFont('Arial', 30)


track_font = pg.font.SysFont('Arial', 30)
track_text = track_font.render("Track:", False, "white")

mode_font = pg.font.SysFont('Arial', 30)

track_numbers = [track_font.render('1', False, "white"),
                 track_font.render('2', False, "white"),
                 track_font.render('3', False, "white"),
                 track_font.render('4', False, "white"),
                 track_font.render('5', False, "white"),
                 track_font.render('6', False, "white"),
                 track_font.render('7', False, "white"),
                 track_font.render('8', False, "white")]

