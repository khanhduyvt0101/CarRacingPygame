import pygame


class cText():
    """
        Display text
        :param text: String, the text to display
        :param font: pygame's system font , font of text
        :return: text displayed
    """

    def __init__(self):
        self.textsurface = None
        self.black = (0, 0, 0)

    def Create(self, text, font):
        self.textsurface = font.render(text, True, self.black)
        return self.textsurface, self.textsurface.get_rect()
