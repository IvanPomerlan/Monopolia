
import pygame
import sys
import random




pygame.init()

rec = (1008, 1008)

screen = pygame.display.set_mode(rec)
pygame.display.set_caption("Что опять Луна?")

myimagge = pygame.image.load("ggtf.png").convert()         #336
myimagge = pygame.transform.scale(myimagge, (1008, 1008))




class mongolia():
    def __init__(self):
        self.money = 500
        self.hodkubika = 0
        self.krug =0

    def run(self):
        if self.hodkubika > 24:
            self.hodkubika -= 24
            self.money += 200
    def armia(self):
        if self.hodkubika == 7:
            print()
    def Temka(self):
        print()

class Botton:
    def __init__(self, x, y):
          self.x = x
          self.y = y

    def kubik(self, x, y):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x < 477 and x > 524:
                    if y < 477 and y > 524:
                        random.randint(0, 6)




    kubik(477, 534)

































