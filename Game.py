# Imports 
import pygame
import random
import time 
from classes import Nota
from assets import *

# Inicialização 
pygame.init()
font = pygame.font.SysFont(None,48)

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









