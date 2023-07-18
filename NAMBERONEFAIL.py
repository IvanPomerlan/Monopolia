

import pygame


pygame.init()

MAX_X = 1008
MAX_Y = 1008

screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("Monopolia")

icon = pygame.image.load("ggtf.png")
pygame.display.set_icon(icon)


def run_game():
    game = True

    while game:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()





pygame.display.flip()
run_game()