

import pygame
import random
import  sys

MAX_X = 1200
MAX_Y = 900
MAX_SNOW = 100
MAX_SIZE = 44

class Snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_nam = random.randint(1, 4)
        self.imag_filename = "snow" + str(self.img_nam) + ".png"
        self.image = pygame.image.load(self.imag_filename)
        self.image =pygame.transform.scale(self.image, (MAX_SIZE, MAX_SIZE))

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = (0 - MAX_SIZE)

        i = random.randint(1, 3)
        if i  == 1:
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - MAX_SIZE)
        elif i  == 2:
            self.x -= 1
            if self.x < (0 - MAX_SIZE):
                self.x = MAX_X

    def drav_snow(self):
        screen.blit(self.image, (self.x, self.y))

def initialize_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        xx = random.randint(0, MAX_Y)
        yy = random.randint(0, MAX_X)
        snowfall.append(Snow(xx, yy))

def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.K_DOWN:
            sys.exit()
#----------------------------- MAIN ------------------------------

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
bg_color = (0, 100, 0)
snowfall = []


initialize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.drav_snow()
    pygame.display.flip()














