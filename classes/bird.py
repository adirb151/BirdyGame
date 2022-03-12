import pygame as py
from constants import *


class Bird:

    def __init__(self):
        img = py.image.load(BIRD_PATH)
        self.img = py.transform.scale(img, (BIRD_WIDTH, BIRD_HEIGHT))
        self.pos_x = BIRD_START_POS_X
        self.pos_y = BIRD_START_POS_Y
        self.direction = 'right'
        self.curr_acceleration = ACCELERATION_SIZE

    def set_speed(self):
        self.pos_y += self.curr_acceleration
        self.curr_acceleration += ACCELERATION_SIZE
        if self.direction == 'right':
            self.pos_x += BIRD_SPEED_X
        else:
            self.pos_x -= BIRD_SPEED_X

    def jump(self):
        self.curr_acceleration = JUMP_SPEED

    def switch_direction(self):
        if self.direction == 'right':
            self.direction = 'left'
        else:
            self.direction = 'right'
        self.img = py.transform.flip(self.img, True, False)

    def touched_spike(self, spike):
        bird_rect = py.Rect(self.pos_x, self.pos_y, BIRD_WIDTH, BIRD_HEIGHT)
        spike_rect = py.Rect(spike.pos_x, spike.pos_y, SPIKE_WIDTH, SPIKE_HEIGHT)
        if bird_rect.colliderect(spike_rect):
            return True
        return False
