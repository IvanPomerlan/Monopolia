import pygame


pygame.init()

rec = (1008, 1008)

screen = pygame.display.set_mode(rec)
pygame.display.set_caption("Что опять Луна?")

myimagge = pygame.image.load("ggtf.png").convert()         #336
myimagge = pygame.transform.scale(myimagge, (1008, 1008))


witdth = screen.get_width()

height = screen.get_height()

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


while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if witdth / 2 <= mouse[0] <= witdth / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()
        screen.fill((60, 25, 60))
    screen.fill((60, 25, 60))

    mouse = pygame.mouse.get_pos()
    if witdth/2 <= mouse[0] <= witdth/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,[witdth/2, height/2, 140, 40])
    else:
        pygame.draw.rect(screen, [witdth/2, height/2, 140, 40])

    screen.blit((witdth/2+5, height/2))
    pygame.display.update()


#----------------------------------------MAIN-------------------------------------------


screen.fill(bd_color)
screen.blit(myimagge, (x, y))
pygame.display.flip()






























