import pygame
from config import *
from sprite import *


class Game:
    def __init__(self):
        self.start = pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.cubes = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()

    def update(self):
        pass

    def draw(self):
        pass

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

                pygame.quit()

    def main(self):
        pass

    def you_died(self):
        pass

    def title_card(self):
        pass


if __name__ == '__main.py__':
    Game()
