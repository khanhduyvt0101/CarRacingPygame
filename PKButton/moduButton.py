import pygame


class cButton():
    """
        Create new button for UI
        :param msg: String, text label
        :param x: double, position X
        :param y: double, position Y
        :param w: double, button width
        :param h: double, button height
        :param ic: tuple, color when not press
        :param ac: tuple, color when pressed
        :param action: function, action when button clicked
        :return: do action when button clicked
        """

    def __init__(self, gameDisplay):
        self.mouse = None
        self.click = None
        self.smallText = None
        self.textSurf = None
        self.textRect = None
        self.black = (0, 0, 0)
        self.gameDisplay = gameDisplay

    def Create(self, msg, x, y, w, h, ic, ac,  action=None):

        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        print(self.click)
        if x+w > self.mouse[0] > x and y+h > self.mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac, (x, y, w, h))

            if self.click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.gameDisplay, ic, (x, y, w, h))

        self.smallText = pygame.font.SysFont("comicsansms", 20)
        self.textSurf, self.textRect = self.instantiate_text(
            msg, self.smallText)
        self.textRect.center = ((x+(w/2)), (y+(h/2)))
        self.gameDisplay.blit(self.textSurf, self.textRect)

    def instantiate_text(self, text, font):
        textsurface = font.render(text, True, self.black)
        return textsurface, textsurface.get_rect()
