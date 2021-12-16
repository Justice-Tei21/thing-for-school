import pygame
from pygame import draw
from main import *


class entity:
    def __init__(self, screen, x, y, width, height, vel, image):
        self.screen = screen
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        self.vel = vel
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.x = self.x
        self.rect.y = self.y


class Hostiles:
    def __init__(self, screen, x, y, width, height, vel, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def target(self, player):
        self.player = Hero(screen, 200, 300, PLAYER_WIDTH, PLAYER_HEIGHT, 6, 'static.png')
        self.target = False
        self.rect.x = player


class Hero(entity):

    def player_movement(self):
        keys_pressed=pygame.key.get_pressed()

        if keys_pressed[pygame.K_d] and self.rect.x + self.width < WIDTH:  # höger
            self.rect.x = self.rect.x + VEL
        if keys_pressed[pygame.K_w] and self.rect.y > 0:  # upp
            self.rect.y = self.rect.y - VEL
        if keys_pressed[pygame.K_a] and self.rect.x > 0:  # vänster
            self.rect.x = self.rect.x - VEL
        if keys_pressed[pygame.K_s] and self.rect.y + self.height < HEIGHT:  # ner
            self.rect.y = self.rect.y + VEL


yellow_menace = Hostiles(screen, 20, 20, 45, 45, 10, 'static.png')

