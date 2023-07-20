import pygame



MAX_X = 900
MAX_Y = 900
game_over = False
bd_color = (0, 10, 0)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("Что опять Луна?")

myimagge = pygame.image.load("pngegg.png").convert()
myimagge = pygame.transform.scale(myimagge, (100, 100))

x = 500
y = 100

move_left = False
move_right = False
move_up = False
move_down = False
#----------------------------MAIN Game LOOP----------------------------
while game_over == False:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            pygame.quit()
        if even.type == pygame.KEYDOWN:
            if even.key == pygame.K_ESCAPE:
                game_over = True
            if even.key == pygame.K_LEFT:
                move_left = True
            if even.key == pygame.K_RIGHT:
                move_right = True
            if even.key == pygame.K_UP:
                move_up = True
            if even.key == pygame.K_DOWN:
                move_down = True

        if even.type == pygame.KEYUP:
            if even.key == pygame.K_LEFT:
                move_left = False
            if even.key == pygame.K_RIGHT:
                move_right = False
            if even.key == pygame.K_UP:
                move_up = False
            if even.key == pygame.K_DOWN:
                move_down = False
        if even.type == pygame.MOUSEBUTTONDOWN:
            x, y = even.pos
            if x < 0:
                x = 0
            if x > 800:
                x = 800
            if y < 0:
                y = 0
            if y > 800:
                y = 800
    if move_left == True:
        x -= 1
        if x < 0:
            x = 0
    if move_right == True:
        x += 1
        if x > 800:
            x = 800
    if move_up == True:
        y -= 1
        if y < 0:
            y = 0
    if move_down == True:
        y += 1
        if y > 800:
            y =800



    screen.fill(bd_color)
    screen.blit(myimagge, (x, y))
    pygame.display.flip()