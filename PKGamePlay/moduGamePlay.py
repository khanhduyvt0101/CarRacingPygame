from PKCar import moduCar
from PKEnemyCar import moduEnemy
import pygame


class cGamePlay:
    def __init__(self):
        pygame.init()
        # Setup window game
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None

        self.initialize()  # Init Function

    def initialize(self):
        self.crashed = False

        # Init Car
        self.car = moduCar.cCar(self.display_width, self.display_height)

        # Init Enemy
        self.enemycar = moduEnemy.cEnemyCar()

        # init Background
        self.bgImg = pygame.image.load(".\\Resources\\back_ground.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

    def drawcar(self, car_x_coordinate, car_y_coordinate):
        self.gameDisplay.blit(
            self.car.getImg(), (car_x_coordinate, car_y_coordinate))
