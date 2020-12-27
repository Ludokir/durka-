import pygame as pg
from os import environ
import sys

environ['SDL_VIDEO_WINDOW_POS'] = '0,30'

pg.init()

screen_size = screen_width, screen_height = (1920, 1080)
screen = pg.display.set_mode(screen_size)

BG = (200, 128, 128)


def quit():
    sys.exit(0)


class Button():
    def __init__(self):
        self.stop = True
        self.image = pg.image.load('textures/button.png')

    def blit(self, x, y, text, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        self.rect = self.image.get_rect(topleft=(x, y))

        if x < mouse[0] < x + self.rect[2] and y < mouse[1] < y + self.rect[3]:
            self.stop = False
            if click[0] == 1 and action is not None:
                action()
        else:
            self.stop = True

        screen.blit(self.image, self.rect)

        font = pg.font.Font('BebasNeue.ttf', 80)
        font_render = font.render(
            text, True, (0, 0, 0) if self.stop else (255, 255, 255))
        font_rect = font_render.get_rect(center=(
            (x + self.rect.w // 2 + 4), (y + self.rect.h // 2 + 4)))
        screen.blit(font_render, font_rect)


def bt_st(text, x, y, action):
    button = Button()
    button.blit(x, y, text, action)
