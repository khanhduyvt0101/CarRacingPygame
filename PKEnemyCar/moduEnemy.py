import pygame
import random
from PKCar import moduCar


class cEnemyCar(moduCar.cCar):
    def __init__(self):
        self.Imgp = pygame.image.load('.\\Resources\\enemy_car_1.png')
        self.X = random.randrange(310, 450)
        self.Y = -600
        self.Speed = 5
        self.Width = 49
        self.Height = 100

    def getSpeed(self):
        return self.Speed

    def getHeight(self):
        return self.enemy_car_height
