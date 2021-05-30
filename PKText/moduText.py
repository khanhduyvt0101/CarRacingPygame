import pygame


class cText():
    """
    A class to represent UI Text object

    Attributes
    ------
    textsurface : pygame's font
        attribute for pygame creating UI Text
    black : tuple
        color used for text

    Methods
    ------
    Create(text,font):
        Python method to display text
    """

    def __init__(self):
        self.textsurface = None
        self.black = (0, 0, 0)

    def Create(self, text, font):
        """
        Display text
        :param text: String, the text to display
        :param font: pygame's system font , font of text
        :return: materials for python display text
        """
        self.textsurface = font.render(text, True, self.black)
        return self.textsurface, self.textsurface.get_rect()
