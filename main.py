import pygame as pg
from os import environ
from menu import *
from settings import *

environ['SDL_VIDEO_WINDOW_POS'] = '0,30'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pg.init()

screen_size = screen_width, screen_height = (1920, 1080)
screen = pg.display.set_mode(screen_size)

BG = pg.image.load('textures/paper.jpg')
BG_rect = BG.get_rect()

room = pg.image.load('textures/room.png')
room_rect = room.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))


class Durka(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('textures/sanitar.png')
        self.rect = self.image.get_rect(
            center=(screen_size[0] // 2, screen_size[1] // 2))
        self.speedx = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.image = pg.image.load('textures/sanitar.png')
        keystate = pg.key.get_pressed()
        if self.rect.right >= 1370 and self.rect.right <= 1410:
            self.image = pg.image.load('textures/skibid_right.png')
        if self.rect.left <= 532 and self.rect.left >= 500:
            self.image = pg.image.load('textures/skibid_left.png')
        if keystate[pg.K_LEFT]:
            self.image = pg.image.load('textures/skibid_left.png')
            self.speedx = -4
            if self.rect.left <= 515:
                self.speedx = 0
        if keystate[pg.K_RIGHT]:
            self.image = pg.image.load('textures/skibid_right.png')
            self.speedx = 4
            if self.rect.right >= 1400:
                self.speedx = 0
        if keystate[pg.K_UP]:
            self.image = pg.image.load('textures/skibid_back.png')
            self.speedy = -4
            if self.rect.top <= 277:
                self.speedy = 0
        if keystate[pg.K_DOWN]:
            self.speedy = 4
            if self.rect.bottom >= 800:
                self.speedy = 0

        self.rect.x += self.speedx
        self.rect.y += self.speedy


all_sprites = pg.sprite.Group()
player = Durka()
all_sprites.add(player)


run = True
while run:
    speed = speed_x, speed_y = 0, 0
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        elif e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                run = False

    all_sprites.update()
    screen.blit(BG, BG_rect)
    screen.blit(room, room_rect)
    all_sprites.draw(screen)
    pg.display.update()
