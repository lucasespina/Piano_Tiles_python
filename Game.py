import pygame
import random
import time 
from classes import Nota

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
# ASSETS
KEY_WIDTH = 125
KEY_HEIGHT = 150
window = pygame.display.set_mode((KEY_WIDTH*5,HEIGHT))
pygame.display.set_caption("TESTE")
nota_img = pygame.image.load('Files/Img/Tecla.png').convert_alpha()
nota_img = pygame.transform.scale(nota_img, (KEY_WIDTH, KEY_HEIGHT))



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

#nota = pygame.draw.rect(window,(BLACK),(x1,y,KEY_WIDTH,KEY_HEIGHT))

# DADOS



# CONTROLE DE VELOCIDADE
clock = pygame.time.Clock()
FPS = 60
velocity = 15
aceleration = 1


# GRUPOS
all_sprites = pygame.sprite.Group()
# all_black = pygame.sprite.Group()
# all_white = pygame.sprite.Group()
# all_gray = pygame.sprite.Group()

all_notas = pygame.sprite.Group()

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

    # gerando linhas
    while len(all_notas) == 0 or (len(all_notas) < 5 and all_notas.sprites()[-1].rect.y > 0):
        x = random.randint(0, 4) * KEY_WIDTH
        y = -KEY_HEIGHT
        print(x, y)
        n = Nota(nota_img, x, y)
        all_notas.add(n)
        all_sprites.add(n)


    # ATUALIZA POSICAO
    all_sprites.update()


    window.fill((WHITE))
    
    all_sprites.draw(window)
    






    pygame.display.update()

pygame.quit()









