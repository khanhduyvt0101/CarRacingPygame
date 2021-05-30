import random
from time import sleep
import pygame
import pickle

import PKCar.moduCar as Car
import PKEnemyCar.moduEnemy as Enemy

import PKButton.moduButton as Button
import PKText.moduText as Text


class cGamePlay:
    """
    A class to represent the game process

    Attributes
    ------
    pause : bool
        is the game pausing
    display_width/display_height : int
        the game's window display value
    clock : any
        game time attribute from pygame.time.Clock()
    gameDisplay : any
        game display
    csound : any
        game sound attribute from pygame.mixer.Sound()

    Methods
    ------
    game_init():
        Constructs all game environment indeed
    game_intro():
        Display game intro panel in start
    game_start():
        Pygame display and start looping
    game_update():
        Game running
    game_quit():
        Quit pygame and close console
    game_pause():
        Pause the game process
    game_unpause():
        Unpause the game process
    game_over():
        Method for Game over
    play_again():
        Start new game after lose
    draw_background():
        Drawing game background
    draw_player_car(car_x_coordinate, car_y_coordinate):
        Draw player's car
    draw_enemy_car(thingx, thingy):
        Draw enemy's car
    draw_current_score(count):
        Draw player's score
    draw_highest_score(score):
        Draw highest score
    save_highest_score(score):
        Returns and saves new score to device if higher than old one

    --
    """
    pause = False

    def __init__(self):
        """
        Constructs all the necessary attributes for the gameplay object

        :return: game's window setup
        """

        pygame.init()

        # Setup window game
        self.display_width = 800
        self.display_height = 600
        self.clock = pygame.time.Clock()
        self.gameDisplay = None

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (192, 192, 192)
        self.green = (0, 200, 0)
        self.red = (200, 0, 0)
        self.bright_green = (0, 255, 0)
        self.yellow = (200, 200, 0)
        self.bright_red = (255, 0, 0)
        self.white = (255, 255, 255)

        self.csound = pygame.mixer.Sound(".\\sound\\crash.wav")

        # Init Function
        self.game_init()

    # game processing section
    def game_init(self):
        """
        Constructs all game environment indeed
        :return: all game environment constructed
        """
        self.crashed = False

        # Init Car
        self.car = Car.cMyCar(self.display_width, self.display_height)

        # Init Enemy
        self.enemycar = Enemy.cEnemyCar()

        # Init Background
        self.bggrass = pygame.image.load(".\\img\\grass.jpg")
        self.bgImg = pygame.image.load(".\\img\\back_ground.jpg")
        self.bgracing = pygame.image.load(".\\img\\bgracing.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

        # Init sound
        pygame.mixer.music.load(".\\sound\\jazz.wav")

        # # Init Button Package
        # self.button = Button.cButton()

    def game_intro(self):
        """
        Display game intro panel in start
        :return: game intro panel displayed
        """
        intro = True

        self.gameDisplay = pygame.display.set_mode(
            (self.display_width, self.display_height))

        while intro:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.gameDisplay.fill((19, 182, 232))
            largeText = pygame.font.SysFont("comicsansms", 115)
            text = Text.cText()
            TextSurf, TextRect = text.Create(
                "Car Racing!", largeText)
            TextRect.center = ((self.display_width/2),
                               (self.display_height/2-50))
            self.gameDisplay.blit(TextSurf, TextRect)
            lifebutton = Button.cButton(self.gameDisplay)
            lifebutton.Create("PLAY!", self.display_width / 6 - 50, self.display_height * 4 / 5, 100, 50, self.yellow,
                              self.bright_green,  self.game_start)
            lifebutton.Create("QUIT", self.display_height / 6 + (self.display_width - self.display_width / 3), self.display_height * 4 / 5, 100, 50,
                              self.red, self.bright_red,  self.game_quit)

            pygame.display.update()
            self.clock.tick(60)

    def game_start(self):
        """
        Pygame display and start looping
        :return: pygame display window and start looping
        """
        self.gameDisplay = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption('Racing Car')
        self.game_update()

    def game_update(self):
        """
        Game running
        :return: Do things while game updating per millisecond
        """
        global pause

        pygame.mixer.music.play(-1)

        self.crashed = False

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                # print(event)

                # input tracking
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        self.car.setX(self.car.getX()-50)
                        print("CAR X COORDINATES: %s" % self.car.getX())
                    if (event.key == pygame.K_RIGHT):
                        self.car.setX(self.car.getX()+50)
                        print("CAR X COORDINATES: %s" % self.car.getX())
                    if (event.key == pygame.K_p):
                        pause = True
                        self.game_pause()
                    print("x: {x}, y: {y}".format(
                        x=self.car.getX(), y=self.car.getX()))

            # draw background
            self.gameDisplay.blit(self.bgracing, (0, 0))
            self.draw_background()

            # draw enemy
            self.draw_enemy_car(self.enemycar.getX(), self.enemycar.getY())
            self.enemycar.setY(self.enemycar.getY() + self.enemycar.getSpeed())

            # recycle enemy
            if self.enemycar.getY() > self.display_height:
                self.enemycar.setY(0 - self.enemycar.getHeight())
                self.enemycar.setX(random.randrange(310, 450))

            # draw player's car
            self.draw_player_car(self.car.getX(), self.car.getY())

            # setting score
            self.draw_current_score(self.count)
            self.draw_highest_score(self.save_highest_score(self.count))
            self.count += 1

            # speed up game process
            if (self.count % 100 == 0):
                self.enemycar.setSpeed(self.enemycar.getSpeed() + 1)
                self.bg_speed += 1

            # tracking collision
            if self.car.getY() < self.enemycar.getY() + self.enemycar.getHeight():
                if self.car.getX() > self.enemycar.getX() and self.car.getX() < self.enemycar.getX() + self.enemycar.getWidth() or self.car.getX() + self.car.getWidth() > self.enemycar.getX() and self.car.getX() + self.car.getWidth() < self.enemycar.getX() + self.car.getWidth():
                    self.crashed = True
                    self.game_over()

            if self.car.getX() < 310 or self.car.getX() > 460:
                self.crashed = True
                self.game_over()

            pygame.display.update()
            self.clock.tick(60)

    def game_quit(self):
        """
        Quit pygame and close console
        :return: pygame call quit()
        """
        pygame.quit()
    # end game processing section

    # game process control
    def game_pause(self):
        """
        Pause the game process
        :return: the game process pause for a while
        """
        pygame.mixer.music.pause()

        # check if user quit while pausing
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # game display pausing panel
            self.gameDisplay.fill(self.yellow)
            largeText = pygame.font.SysFont("comicsansms", 115)
            text = Text.cText()
            TextSurf, TextRect = text.Create("Paused", largeText)
            TextRect.center = ((self.display_width/2), (self.display_height/2))
            self.gameDisplay.blit(TextSurf, TextRect)
            lifebutton = Button.cButton(self.gameDisplay)
            lifebutton.Create("Continue", self.display_width / 6 - 50, self.display_height * 4 / 5, 100, 50, self.green,
                              self.bright_green, self.game_unpause)
            lifebutton.Create("Quit", self.display_height / 6 + (self.display_width - self.display_width / 3), self.display_height * 4 / 5, 100, 50,
                              self.red, self.bright_red, self.game_quit)

            pygame.display.update()
            self.clock.tick(60)

    def game_unpause(self):
        """
        Unpause the game process
        :return: the game process continue
        """
        global pause
        pygame.mixer.music.unpause()
        pause = False

    def game_over(self):
        """
        Method for Game over
        :return: Acts when player crashed
        """

        # check the score
        self.save_highest_score(self.count)

        # music change
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(self.csound)

        # game over display
        self.gameDisplay.fill(self.yellow)

        # game over display panel
        largeText = pygame.font.SysFont("comicsansms", 115)
        nomarlText = pygame.font.SysFont("comicsansms", 40)
        temptext = Text.cText()
        TextSurf, TextRect = temptext.Create("You Crashed", largeText)
        TextRect.center = ((self.display_width/2), (self.display_height/4))
        temptext2 = Text.cText()
        TextSurf1, TextRect1 = temptext2.Create(
            "Your score: " + str(self.count), nomarlText)
        TextRect1.center = ((self.display_width/2), (self.display_height/2.5))
        temptext3 = Text.cText()
        TextSurf2, TextRect2 = temptext3.Create(
            "Best score: " + str(self.save_highest_score(self.count)), nomarlText)
        TextRect2.center = ((self.display_width/2), (self.display_height/2))

        self.gameDisplay.blit(TextSurf, TextRect)
        self.gameDisplay.blit(TextSurf1, TextRect1)
        self.gameDisplay.blit(TextSurf2, TextRect2)

        # check if user quit game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            lifebutton = Button.cButton(self.gameDisplay)
            lifebutton.Create("Play Again", self.display_width / 6 - 50, self.display_height * 4 / 5, 100, 50, self.green,
                              self.bright_green, self.play_again)
            lifebutton.Create("Quit", self.display_height / 6 + (self.display_width - self.display_width / 3), self.display_height * 4 / 5, 100, 50,
                              self.red, self.bright_red, self.game_quit)

            pygame.display.update()
            self.clock.tick(60)

    def play_again(self):
        """
        Start new game after lose
        :return: start a new game process
        """
        # sleep(1)
        car_racing.game_init()
        car_racing.game_update()
    # end game process control

    # objects

    # game render section

    def draw_background(self):
        """
        Drawing game background
        :return: game background drew
        """
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def draw_player_car(self, car_x_coordinate, car_y_coordinate):
        """
        Draw player's car
        :param car_x_coordinate: Car position X
        :param car_y_coordinate: Car position Y
        :return: Car drew by image itself
        """
        self.gameDisplay.blit(
            self.car.getImg(), (car_x_coordinate, car_y_coordinate))

    def draw_enemy_car(self, thingx, thingy):
        """
        Draw enemy's car
        :param thingx: int, Car Position X
        :param thingy: int, Car Position Y
        :return: Enemy's car drew
        """
        self.gameDisplay.blit(self.enemycar.getImg(), (thingx, thingy))

    def draw_current_score(self, count):
        """
        Draw player's score
        :param count: int, current score
        :return: Player's score drew
        """
        font = pygame.font.SysFont("arial", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (5, 0))

    def draw_highest_score(self, score):
        """
        Draw highest score
        :param score: int, highest score
        :return: Highest score drew
        """
        font = pygame.font.SysFont("arial", 30)
        text = font.render("Top score : " + str(score), True, self.white)
        self.gameDisplay.blit(text, (5, 20))
    # end game render section

    # infernal
    def save_highest_score(self, score):
        """
        Returns and saves new score to device if higher than old one
        :param score: int, new score
        :return: new highest score
        """
        # load the previous score if it exists
        try:
            with open('score.dat', 'rb') as file:
                temp = pickle.load(file)
        except:  # save the score
            with open('score.dat', 'wb') as file:
                pickle.dump(score, file)
            temp = 0

        if temp < score:
            temp = score
            with open('score.dat', 'wb') as file:
                pickle.dump(temp, file)

        return temp


car_racing = cGamePlay()
car_racing.game_intro()
# car_racing.Game_loop()
# pygame.quit()
# quit()
