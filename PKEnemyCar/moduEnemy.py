

from Car import cCar
import pygame
import random


class cEnemyCar(cCar):
    def __init__(self):
        self.Imgp = pygame.image.load('.\\img\\enemy_car_1.png')
        self.X = random.randrange(310, 450)
        self.Y = -600
        self.Speed = 5
        self.Width = 49
        self.Height = 100

    def getSpeed(self):
        return self.Speed

    def setSpeed(self, speed):
        self.Speed = speed

    def getHeight(self):
        return self.Height
