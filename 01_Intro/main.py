import pygame
from settings import * 
from board import *

class Game(object):

    def __init__(self) -> None:
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(CAP)
        self.clock = pygame.time.Clock()
    
        self.board = Board()
    
    def run(self):
        while True:
            event_list = pygame.event.get()

            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.board.reverse_it = True
                        print("Map reversed....")
        
            self.board.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()