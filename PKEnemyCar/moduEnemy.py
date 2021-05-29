from Car import cCar
import pygame
import random


class cEnemyCar(cCar):
    """
    A class inherited of cCar, represent for enemy's car

    Attributes
    ------
    Speed : int
        car's speed to go down
    Height : int
        car's height

    Methods
    ------
    getSpeed():
        Returns car's speed
    setSpeed(speed):
        Set the speed of the car
    getHeight():
        Returns car's height

    --
    """

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
