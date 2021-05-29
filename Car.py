import pygame


class cCar:
    """
    A class to represent a car

    Attributes
    ------
    Imgp : pygame image
        car's image
    X : int
        car's position X
    Y : int
        car's position Y
    Width : int
        car's width

    Methods
    ------
    getImg():
        Returns car's image
    getX():
        Returns car's position X
    getY():
        Returns car's position Y
    getWidth():
        Returns car's width
    setX():
        Set the position X of the car
    setY():
        Set the position Y of the car

    --
    """
    def __init__(self):
        self.Imgp = None
        self.X = None
        self.Y = None
        self.Width = None

    def getImg(self):
        """
        Returns car's image
        :return: car's image
        """
        return self.Imgp

    def getX(self):
        """
        Returns car's position X
        :return: car's position X
        """
        return self.X

    def getY(self):
        """
        Returns car's position Y
        :return: car's position Y
        """
        return self.Y

    def getWidth(self):
        """
        Returns car's width
        :return: car's width
        """
        return self.Width

    def setX(self, X):
        """
        Set the position X of the car
        :param X: new position X
        :return: position X of the car is set
        """
        self.X = X

    def setY(self, Y):
        """
        Set the position Y of the car
        :param Y: new position Y
        :return: position Y of the car is set
        """
        self.Y = Y
