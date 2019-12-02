import pygame
class Cell():
    def __init__(self, rect, x, y, l=(0,0,0)):
        self.c = l
        self.rect = rect
        self.posx = x
        self.posy = y
        self.count = 0

    def iteration(self):
        if self.count < 2 or self.count > 3:
            self.c = (0, 0, 0)
        elif self.count == 3:
            self.c = (255, 255, 255)

        self.count = 0
