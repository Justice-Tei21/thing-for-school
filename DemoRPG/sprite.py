import pygame
from config import *
import main
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
    def draw(self):
        pass
    def update(self):
        pass
    