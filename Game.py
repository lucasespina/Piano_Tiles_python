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
        print(x, y)
        n = Nota(nota_img, x, y)
        all_notas.add(n)
        all_sprites.add(n)

    
    
    #Tecla Clicada
    certo = False
    for nota in all_notas:
        if pos:
            if nota.rect.collidepoint(pos):
                nota.img(nota_img_clicada)
                certo = certo or True
    if pos and not certo:
        print("errou")
    
    
    # Som ao clicar na nota (não está funcionando ainda)

    # from pygame import *

    #     mixer.init()
    #     mixer.music.load('musica.wav')
    #     mixer.music.set_volume(0.7)
    #     mixer.music.play()

    #     while True:

    #         if nota.rect.collidepoint(pos):
    #             mixer.music.pause()    
    #         else:
    #             mixer.music.unpause()
    #             time.sleep(100)
    #         break
                

    
    # ATUALIZA POSICAO
    all_sprites.update()
    

    window.fill((WHITE))
    
    all_sprites.draw(window)


    pygame.display.update()



pygame.quit()









