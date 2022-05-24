import pygame
class Nota(pygame.sprite.Sprite):
    def __init__(self,correta,cor, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width = 125
        self.height = 150
        self.x = x
        self.y = y
        self.color = cor
        self.correta = correta

    def update(self,aceleracao):
        self.y += aceleracao
        if self.y > 600:
            self.kill()
