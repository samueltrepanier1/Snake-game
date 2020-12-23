import pygame
import sys
import random


class Snake():

    def __init__(self):
        pass

    def get_head_position(self):
        pass

    def turn(self, point):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def draw(self, surface):
        pass

    def handle_keys(self):
        pass


class Food(object):

    def __init__(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass


SCREEN_WIDTH = 480
SCREEN_HEIGTH = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGTH = SCREEN_HEIGTH / GRIDSIZE

UP = (0,-1)
DOWN= (0,1)
LEFT = (-1,0)
RIGTH = (1,0)


def main():
    pygame.init()
    clock = pygame.time.Clock()




main()