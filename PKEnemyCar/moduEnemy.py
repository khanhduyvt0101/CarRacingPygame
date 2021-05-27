

import pygame
import random


class cEnemyCar():
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

    def getImg(self):
        return self.Imgp

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getWidth(self):
        return self.Width

    def setX(self, X):
        self.X = X

    def setY(self, Y):
        self.Y = Y
