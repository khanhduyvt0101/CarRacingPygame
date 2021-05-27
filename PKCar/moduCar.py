import pygame


class cCar:
    def __init__(self, display_Width, display_Height):
        self.Imgp = pygame.image.load('.\\img\\car.png')
        self.X = (display_Width * 0.45)
        self.Y = (display_Height * 0.8)
        self.Width = 49

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
