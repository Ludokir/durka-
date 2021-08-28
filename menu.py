from settings import *
import pygame as pg
import sys
stop = False
begin = False


def name():
    font = pg.font.Font('BebasNeue.ttf', 100)
    font_render = font.render('ESCAPE FROM DURKA', True, (0, 0, 0))
    font_rect = font_render.get_rect(center=((1920 // 2), 100))
    screen.blit(font_render, font_rect)


def starter():
    global begin
    begin = True


def menu():
    global stop
    stop = False


def settings():
    global stop
    stop = True
    if stop:
        label = pg.image.load('textures/settings.png')
        label_rect = label.get_rect(center=((1920 // 2), 200))
        screen.blit(label, label_rect)
        bt_st('BACK', 50, (screen_height - label_rect[3] - 50), menu)


run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit(0)
        elif e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                sys.exit(0)

    screen.fill(BG)

    if not stop:
        bt_st('START', 1350, 650, starter)
        bt_st('SETTINGS', 1350, 750, settings)
        bt_st('QUIT', 1350, 850, quit)
    if stop:
        settings()
    if begin:
        run = False
    name()

    pg.display.update()
