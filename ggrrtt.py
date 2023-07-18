

import pygame

import sys

pygame.init()

rec = (700, 700)

screen = pygame.display.set_mode(rec)

color = (255, 255, 255)

color_light = (170, 170, 170)

color_dark = (100, 100, 100)

witdth = screen.get_width()

height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel', 35)

text = smallfont.render('quit', True, color)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if witdth/2 <= mouse[0] <= witdth/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
    screen.fill((60, 25, 60))

    mouse = pygame.mouse.get_pos()
    if witdth/2 <= mouse[0] <= witdth/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, color_light, [witdth/2, height/2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [witdth/2, height/2, 140, 40])

    screen.blit(text, (witdth/2+5, height/2))
    pygame.display.update()

