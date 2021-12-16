import pygame
from config import *
from sprite import *

class game:
    def __init__(self):
        self.start= pygame.init()
        self.running = True
        self.screen= pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

    def main(self):
        self.new()
    def new(self):
        self.start
        self.screen
        while self.running==True:
            pygame.display.update()
    def update(self):
        pygame.display.update()
    def draw(self):
        pass
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False
                pygame.quit()


if __name__ == '__main.py__':
    game.main()