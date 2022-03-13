import pygame as py
from constants import *
import random


class Bonus:
    def __init__(self):
        self.pos_x = random.randint(SPIKE_WIDTH, WINDOW_WIDTH - SPIKE_WIDTH)
        self.pos_y = random.randint(SPIKE_HEIGHT, WINDOW_HEIGHT - SPIKE_HEIGHT)
        img = py.image.load(BONUS_PATH)
        self.img = py.transform.scale(img, (BONUS_WIDTH, BONUS_HEIGHT))
