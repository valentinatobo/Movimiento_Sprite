from Character import *
from jugador import Base_Jugador
import pygame
from pygame.sprite import Sprite
from pygame import*


class Jugador_adapter(Base_Jugador, Character):
    
    def __init__(self):
        Sprite.__init__(self)
        self.direction = 0
        self.cont = 0
        self.speed = 20
        self.movementLeft = True
        self.movementRight = True
        
    def defPositions(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY

    def set_sprites(self, sprites):
        self.set_sprite(sprites)

    def mover_derecha(self):
        self.moveRight()

    def mover_izquierda(self):
        self.moveLeft()

    def update(self):
        self.changeSprite() 

    def draw(self, screen):
        self.drawCharacter(screen) 
