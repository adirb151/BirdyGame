import pygame
import random

from classes.bird import Bird
from classes.file_reader import Reader
from classes.spike import Spike
from constants import *


class Manager:

    def __init__(self, screen):
        self.game_on = False
        self.game_over = False
        self.screen = screen
        self.bird = Bird()
        self.spikes = []
        self.flip_spikes_side = False
        self.score = 0
        self.reader = Reader()
        self.best_score = self.reader.best_score

    def show_background(self):
        pygame.draw.rect(self.screen, BLACK_COLOR, pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))

    def show_bird(self):
        self.screen.blit(self.bird.img, (self.bird.pos_x, self.bird.pos_y))

    def set_speed(self):
        self.bird.set_speed()

    def jump(self):
        self.bird.jump()

    def check_wall(self):
        if self.bird.direction == 'right' and self.bird.pos_x >= WINDOW_WIDTH - BIRD_WIDTH:
            return True
        elif self.bird.direction == 'left' and self.bird.pos_x <= 0:
            return True
        else:
            return False

    def switch_direction(self):
        self.bird.switch_direction()

    def show_game_over(self):
        if not self.game_over:
            font = pygame.font.SysFont(START_TEXT_FONT, START_TEXT_SIZE)
            self.screen.blit(font.render(START_TEXT, True, WHITE_COLOR), (START_TEXT_POS_X, START_TEXT_POS_Y))
        else:
            font = pygame.font.SysFont(END_TEXT_FONT, END_TEXT_SIZE)
            self.screen.blit(font.render(END_TEXT, True, WHITE_COLOR), (END_TEXT_POS_X, END_TEXT_POS_Y))

    def bird_fell(self):
        if self.bird.pos_y >= WINDOW_HEIGHT - BIRD_HEIGHT or self.bird.pos_y <= 0:
            return True
        return False

    def spikes_collide(self, y_val):
        for spike in self.spikes:
            if spike.pos_y <= y_val <= spike.pos_y + SPIKE_HEIGHT:
                return True
        return False

    def show_spikes(self, should_replace):
        if should_replace:
            self.spikes = []
            if self.bird.direction == 'right':
                x_pos = WINDOW_WIDTH - SPIKE_WIDTH
            else:
                x_pos = 0
            for i in range(SPIKES_NUM):
                rand_y = random.randint(0, WINDOW_HEIGHT - SPIKE_HEIGHT)
                while self.spikes_collide(rand_y):
                    rand_y = random.randint(0, WINDOW_HEIGHT - SPIKE_HEIGHT)
                new_spike = Spike(x_pos, rand_y, self.flip_spikes_side)
                self.spikes.append(new_spike)
        for spike in self.spikes:
            self.screen.blit(spike.img, (spike.pos_x, spike.pos_y))

    def touched_spike(self):
        for spike in self.spikes:
            if self.bird.touched_spike(spike):
                return True
        return False

    def show_score(self):
        font = pygame.font.SysFont(SCORE_TEXT_FONT, SCORE_TEXT_SIZE)
        self.screen.blit(font.render(SCORE_TEXT + str(self.score), True, WHITE_COLOR),
                         (SCORE_TEXT_POS_X, SCORE_TEXT_POS_Y))

        font = pygame.font.SysFont(BEST_SCORE_TEXT_FONT, BEST_SCORE_TEXT_SIZE)
        self.screen.blit(font.render(BEST_SCORE_TEXT + self.best_score, True, WHITE_COLOR),
                         (BEST_SCORE_TEXT_POS_X, BEST_SCORE_TEXT_POS_Y))

    def add_score(self):
        self.score += SCORE_ADDITION

    def update_best_score(self):
        if self.score > int(self.best_score):
            self.reader.update_best_score(str(self.score))

