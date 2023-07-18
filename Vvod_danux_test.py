import pygame
def battons(self, action=None):
    for ev in pygame.event.get():
        mouses = pygame.mouse.get_pos()
        if ev.type == pygame.MOUSEMOTION:
            if self.x <= mouses[0] <= self.xx and self.y <= mouses[1] <= self.yy:
                return screen.blit(self.image, (self.x, self.y))
            else:
                screen.blit(self.image_fon, (self.xxx, self.yyy))

            pygame.display.update()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.x <= mouses[0] <= self.xx and self.y <= mouses[1] <= self.yy:
                if action is not None:
                    pygame.time.delay(100)
                    action()
                    pygame.display.update()
            else:
                screen.blit(self.image_fon, (self.xxx, self.yyy))









