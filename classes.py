import pygame

class Nota(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        super(Nota, self).__init__()
        
        
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.aceleracao = 5
        self.color = "Preto"

    def update(self):
        
        self.rect.y += self.aceleracao
        if self.rect.y > 600:
            self.kill()
            
    def img(self,img, x , y):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.aceleracao = 5
        self.color = "Roxo"
