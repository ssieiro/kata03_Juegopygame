import pygame as pg
from pygame.locals import *
import sys
import random

_fps = 60

class Ball(pg.Surface):
    x = 0
    y = 0
    color = (255, 255, 255)
    velocidad = 5
    dirx = velocidad
    diry = velocidad

    def __init__(self):
        pg.Surface.__init__(self, (16,16))
        self.fill(self.color)

    def setColor(self, color):
        self.color = color
        self.fill(self.color)

    def avanza(self):
        if self.x >= 800:
            self.dirx = -self.velocidad
        if self.x <= 0:
            self.dirx = self.velocidad
        if self.y >= 600:
            self.diry = -self.velocidad
        if self.y <= 0:
            self.diry = self.velocidad

        self.x += self.dirx
        self.y += self.diry

    def comprobarChoque(self, candidata):
        choqueX = candidata.x >= self.x and candidata.x <= self.x+16 or \
            candidata.x+16 >= self.x and candidata.x+16 <= self.x+16
        choqueY = candidata.y >= self.y and candidata.y <= self.y+16 or \
            candidata.y+16 >= self.y and candidata.y+16 <= self.y+16
        
        if choqueX and choqueY:
            self.dirx = self.dirx * -1

        # Como es una condición devuelve True o False por lo que no hace falta hacer un if

class Game:
    clock = pg.time.Clock()

    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pg.display
        self.screen = self.display.set_mode(self.size)
        self.screen.fill((60, 60, 60))
        self.display.set_caption('Mi juego')

        self.ball1 = Ball()
        self.ball1.setColor((255,0,0))
        self.ball1.x = random.randrange(800)
        self.ball1.y = random.randrange(600)
        self.ball1.velocidad = random.randrange(4, 9)

        self.ball2 = Ball()
        self.ball2.setColor((255,255,0))
        self.ball2.x = random.randrange(800)
        self.ball2.y = random.randrange(600)
        self.ball2.velocidad = random.randrange(4, 9)

    def start(self):
        while True:
            self.clock.tick(_fps)

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            #Modifica la posición de ball
            self.ball1.avanza()
            self.ball2.avanza()

            self.ball1.comprobarChoque(self.ball2)
            self.ball2.comprobarChoque(self.ball1)

            #Pintar los sprites en screen
            self.screen.fill((60,60,60))

            # blit coloca la bola en la pantalla en la posición que le demos

            self.screen.blit(self.ball1, (self.ball1.x, self.ball1.y))
            self.screen.blit(self.ball2, (self.ball2.x, self.ball2.y))

            self.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game(800, 600)
    game.start()
