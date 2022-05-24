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
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TESTE")



# ASSETS
KEY_WIDTH = 125
KEY_HEIGHT = 150
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

nota = pygame.draw.rect(window,(BLACK),(x1,y,KEY_WIDTH,KEY_HEIGHT))

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
list_notas = []

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
    if len(list_notas) == 0 or list_notas[0][0].rect.y >= 0:
        novas_notas = []
        for i in range(4):
            nota = Nota(False, BLACK, KEY_WIDTH * i, -KEY_HEIGHT)
            novas_notas[i] = nota
            all_notas.add(nota)
            all_sprites.add(nota)
        list_notas.insert(0, novas_notas)

    while len(list_notas) > 4:
        del list_notas[-1]


    # ATUALIZA POSICAO
    all_sprites.update()


    window.fill((WHITE))
    
    






    pygame.display.update()

pygame.quit()









