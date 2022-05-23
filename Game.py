import pygame
import random
import time 

pygame.init()

# CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
LIGHT_BLUE = (0, 255, 255)


# DISPLAY
WIDTH = 500
HEIGHT = 600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TESTE")



# ASSETS
KEY_WIDTH = 125
KEY_HEIGHT = 150
velocity = 15
aceleration = 1
font = pygame.font.SysFont(None,48)
x1 = 0
x2 = 0 + KEY_WIDTH
x3 = 0 + (2*KEY_WIDTH)
x4 = 0 + (3*KEY_WIDTH)
y = 0 - KEY_HEIGHT
y1 = 0 - KEY_HEIGHT
y2 = 0 - 2 * KEY_HEIGHT
y3 = 0 - 3 * KEY_HEIGHT
y4 = 0 - 4 * KEY_HEIGHT
xposicoes = [x1,x2,x3,x4]
yposicoes = [y1,y2,y3,y4]


# DADOS
class Keys(pygame.sprite.Sprite):
    def __init__(self, formato):
        pygame.sprite.Sprite.__init__(self)

        self.image = formato
        self.rect.y = random.randint(xposicoes)
        self.speedy = random.randint(velocity)
    
    def update(self):
        self.rect.y += self.speedy



# CONTROLE DE VELOCIDADE
clock = pygame.time.Clock()
FPS = 60

# GRUPOS
all_sprites = pygame.sprite.Group()
all_black = pygame.sprite.Group()
all_white = pygame.sprite.Group()
all_gray = pygame.sprite.Group()







# JOGO
game = True
while game:
    clock.tick(FPS)

    # EVENTOS
    for event in pygame.event.get():
        # EXIT
        if event.type == pygame.QUIT:
            game = False
        # TOQUE
        touch = pygame.mouse.get_pressed


    # ATUALIZA POSICAO
    all_sprites.update()


    # VERIFICA NOTA PASSAR
    # if nota > HEIGHT:
    # time.sleep(5)
    # game = False



    window.fill((WHITE))
    
    pygame.draw.rect(window,(BLACK),(x1,y,KEY_WIDTH,KEY_HEIGHT))
    






    pygame.display.update()

pygame.quit()