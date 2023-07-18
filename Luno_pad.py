

import pygame
import random

max_x = 1200
max_y = 900



game_over = False
bd_color = (0, 10, 0)

pygame.init()
screen = pygame.display.set_mode((max_x, max_y))
pygame.display.set_caption("Что опять Луна?")

myimagge = pygame.image.load("pngegg.png")
myimagge = pygame.transform.scale(myimagge, (100, 100))
class dee():
    def __init__(self):
        self.y = self.y
        self.x = self.x
        self.myimagge = self.myimagge
        self.place = self.place
    def ono_samoe(self):
        self.place = random.randint(0, 1100)
        self.y = 0
        self.myimagge = pygame.image.load("pngegg.png")
        self.myimagge = pygame.transform.scale(myimagge, (100, 100))

        while True:
            self.y += 3
            screen.fill(bd_color)
            screen.blit(self.myimagge, (self.place, self.y))
            pygame.display.flip()
            if self.y > 900:
                break
while game_over == False:
    for even in pygame.event.get():
        if even.type == pygame.KEYDOWN:
            if even.key == pygame.K_ESC
                APE:
                game_over = True
            if even.key == pygame.K_UP:
                for x in range(1 , 10):
                    dee.ono_samoe()



