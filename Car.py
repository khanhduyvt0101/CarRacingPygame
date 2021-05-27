import pygame


class cCar:
    def __init__(self):
        self.Imgp = None
        self.X = None
        self.Y = None
        self.Width = None

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
