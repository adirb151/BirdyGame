import pygame as py
from constants import *


class Spike:

    def __init__(self, pos_x, pos_y, should_flip):
        self.pos_x = pos_x
        self.pos_y = pos_y
        img = py.image.load(SPIKE_PATH)
        self.img = py.transform.scale(img, (SPIKE_WIDTH, SPIKE_HEIGHT))
        if should_flip:
            self.img = py.transform.flip(self.img, True, False)
