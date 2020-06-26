import pygame
from pygame.sprite import Sprite
from pygame import *
import time

class Jugador(Sprite):
    
    def __init__(self):
        Sprite.__init__(self)
        self.sentido = 0
        self.velocidad = 5
        self.cont = 0
   
    def defPositions(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY
   
    def set_sprites(self, sprites):
        self.imagenes = sprites
        self.image = self.imagenes[self.sentido][0]
        self.rect = self.image.get_rect()

    def mover_derecha(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_RIGHT]:
            self.rect.x += self.velocidad
            self.sentido = 3

    def mover_izquierda(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.rect.x -= self.velocidad
            self.sentido = 2 

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT] or teclas[K_RIGHT] or teclas[K_UP] or teclas[K_DOWN]:
            self.image = self.imagenes[self.sentido][self.cont]
            self.cont += 1
            self.cont %= 3 

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,250))


class Base_Jugador(Sprite):
    def defPositions(self, auxPosX, auxPosY):
        pass

    def set_sprites(self, images):
        pass

    def mover_derecha(self):
        pass

    def mover_izquierda(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass 



