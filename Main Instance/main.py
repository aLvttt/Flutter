import pygame as pg
import sys

FPS = 60

pg.init()
pg.display.set_mode((640, 560), pg.RESIZABLE) 
clock = pg.time.Clock()

pg.display.update()

while True:
    clock.tick(FPS)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pg.display.update()