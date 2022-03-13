import pygame as py
from constants import *
from classes.manager import Manager

py.init()
screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = py.display.set_mode(screen_size)
clock = py.time.Clock()

manager = Manager(screen)
manager.show_background()
manager.show_bird()
manager.show_spikes(True)
manager.show_score()
manager.show_bonus()

py.display.flip()


def is_finished():
    finished = False
    for event in py.event.get():
        if event.type == py.QUIT:
            finished = True
        if event.type == py.KEYDOWN:
            if not manager.game_on:
                manager.game_on = True
            elif event.key == py.K_SPACE:
                manager.jump()
    if manager.bird_fell() or manager.touched_spike():
        manager.game_on = False
        manager.game_over = True
        manager.update_best_score()
    manager.check_touched_bonus()
    return finished


while not is_finished():
    if manager.game_on:
        manager.set_speed()
    manager.show_background()
    manager.show_bird()
    manager.show_spikes(False)
    manager.show_score()
    manager.show_bonus()
    if manager.check_wall():
        manager.switch_direction()
        manager.flip_spikes_side = not manager.flip_spikes_side
        manager.show_spikes(True)
        manager.add_score()
        manager.refresh_bonus()
    if not manager.game_on:
        manager.show_game_over()
    py.display.flip()
    clock.tick(60)

py.quit()




