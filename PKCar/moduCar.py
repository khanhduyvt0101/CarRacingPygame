import pygame
import Car


class cMyCar(Car.cCar):
    def __init__(self, display_Width, display_Height):
        self.Imgp = pygame.image.load('.\\img\\car.png')
        self.X = (display_Width * 0.45)
        self.Y = (display_Height * 0.8)
        self.Width = 49
