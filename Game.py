# Imports 
import pygame
import random
import time 
from classes import Nota
from assets import *

# Inicialização 
pygame.init()
font = pygame.font.SysFont(None,48)
pos = None
# JOGO
game = True
placar = 0

while game:
    pos = None
    clock.tick(FPS)

    # EVENTOS
    for event in pygame.event.get():
        # EXIT
        if event.type == pygame.QUIT:
            game = False
        # TOQUE
        touch = pygame.mouse.get_pressed
        
        
        #Mouse Posição Click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

    # gerando linhas
    while len(all_notas) == 0 or (len(all_notas) < 5 and all_notas.sprites()[-1].rect.y > 0):
        x = random.randint(0, 4) * KEY_WIDTH
        y = -KEY_HEIGHT
        n = Nota(nota_img, x, y)
        all_notas.add(n)
        all_sprites.add(n)

    
    
    #Tecla Clicada
    certo = False
    for nota in all_notas:
        if pos:
            if nota.rect.collidepoint(pos):
                
                #Mudando a cor da tecla clicada
                nota.img(nota_img_clicada, nota.rect.x, nota.rect.y)
                
                #Aumentando a velocidade após clicar
                FPS = FPS
                
                #Adicionando Score
                placar = placar + 1
                
                
                certo = certo or True
        if nota.rect.y >= 600 and nota.color=="Preto":
            print("errou")
    if pos and not certo:
        print("errou")
        
    # print(placar)

    
    # ATUALIZA POSICAO
    all_sprites.update()
    

    window.fill((WHITE))
    
    all_sprites.draw(window)


    pygame.display.update()



pygame.quit()









