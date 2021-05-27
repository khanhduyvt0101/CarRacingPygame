import random
from time import sleep
import pygame


import PKCar.moduCar as Car
import PKEnemyCar.moduEnemy as Enemy


class cGamePlay:

    def __init__(self):
        pygame.init()
        # Setup window game
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = pygame.display.set_mode(
            (self.display_width, self.display_height))

        self.black = (0, 0, 0)

        self.grey = (192, 192, 192)
        self.green = (0, 200, 0)
        self.red = (200, 0, 0)
        self.bright_green = (0, 255, 0)
        self.yellow = (200, 200, 0)
        self.bright_red = (255, 0, 0)
        self.white = (255, 255, 255)

        self.initialize()  # Init Function

    def initialize(self):
        self.crashed = False

        # Init Car
        self.car = Car.cCar(self.display_width, self.display_height)

        # Init Enemy
        self.enemycar = Enemy.cEnemyCar()

        # init Background
        self.bggrass = pygame.image.load(".\\img\\grass.jpg")
        self.bgImg = pygame.image.load(".\\img\\back_ground.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

    def quitgame(self):
        pygame.quit()

    def text_objects(self, text, font):
        textsurface = font.render(text, True, (0, 0, 0))
        return textsurface, textsurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
        else:
            pygame.draw.rect(self.gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        self.gameDisplay.blit(textSurf, textRect)

    def game_intro(self):
        intro = True

        while intro:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.gameDisplay.fill(self.yellow)
            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = self.text_objects("Watch Out!", largeText)
            TextRect.center = ((self.display_width/2), (self.display_height/2))
            self.gameDisplay.blit(TextSurf, TextRect)

            self.button("GO!", 350, 450, 100, 50,
                        self.green, self.bright_green, self.Game_loop())
            self.button("Quit", 900, 450, 100, 50,
                        self.red, self.bright_red, self.quitgame())

            pygame.display.update()
            self.clock.tick(60)

    def drawcar(self, car_x_coordinate, car_y_coordinate):
        self.gameDisplay.blit(
            self.car.getImg(), (car_x_coordinate, car_y_coordinate))

    def StartGame(self):
        self.gameDisplay = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption('Racing Car')
        self.game_intro()

    def Game_loop(self):

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                # print(event)

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        self.car.setX(self.car.getX()-50)
                        print("CAR X COORDINATES: %s" % self.car.getX())
                    if (event.key == pygame.K_RIGHT):
                        self.car.setX(self.car.getX()+50)
                        print("CAR X COORDINATES: %s" % self.car.getX())
                    print("x: {x}, y: {y}".format(
                        x=self.car.getX(), y=self.car.getX()))

            self.gameDisplay.fill(self.black)
            self.back_ground_raod()

            self.run_enemy_car(self.enemycar.getX(), self.enemycar.getY())
            self.enemycar.setY(self.enemycar.getY() + self.enemycar.getSpeed())

            if self.enemycar.getY() > self.display_height:
                self.enemycar.setY(0 - self.enemycar.getHeight())
                self.enemycar.setX(random.randrange(310, 450))

            self.drawcar(self.car.getX(), self.car.getY())
            self.highscore(self.count)
            self.count += 1
            if (self.count % 100 == 0):
                self.enemycar.setSpeed(self.enemycar.getSpeed() + 1)
                self.bg_speed += 1
            if self.car.getY() < self.enemycar.getY() + self.enemycar.getHeight():
                if self.car.getX() > self.enemycar.getX() and self.car.getX() < self.enemycar.getX() + self.enemycar.getWidth() or self.car.getX() + self.car.getWidth() > self.enemycar.getX() and self.car.getX() + self.car.getWidth() < self.enemycar.getX() + self.car.getWidth():
                    self.crashed = True
                    self.display_message("Game Over !!!")

            if self.car.getX() < 310 or self.car.getX() > 460:
                self.crashed = True
                self.display_message("Game Over !!!")

            pygame.display.update()
            self.clock.tick(60)

    def display_message(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(
            text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(1)
        # car_racing.initialize()
        # car_racing.game_intro()

    def back_ground_raod(self):
        self.gameDisplay.blit(self.bggrass, (0, 0))
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemy_car(self, thingx, thingy):
        self.gameDisplay.blit(self.enemycar.getImg(), (thingx, thingy))

    def highscore(self, count):
        font = pygame.font.SysFont("arial", 20)
        text = font.render("Score : " + str(count), True, self.black)
        self.gameDisplay.blit(text, (0, 0))

    def display_credit(self):
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Thanks for playing!", True, self.white)
        self.gameDisplay.blit(text, (600, 520))


# if __name__ == '__main__':
# car_racing = cGamePlay()
# car_racing.game_intro()
# car_racing.StartGame()
