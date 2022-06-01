# Imports 
import pygame
from pygame import mixer
import random
import time 
from classes import Nota
from assets import *

# Inicialização 
pygame.init()
font = pygame.font.SysFont(None,48)
scoreFont = pygame.font.SysFont(None, 40)

pos = None
# JOGO
game = True
menu = True
menuPreta = False
menuBranca = False
score = 0
highscore = 0

mixer.init()
mixer.music.set_volume(0.2)
sound_wrong = pygame.mixer.Sound('wrong.wav')
sound_hit = 0
sound_hits = [pygame.mixer.Sound('musica.wav')]
#mixer.music.load('musica.mp3')

while game:
    pos = None
    clock.tick(FPS)

    scoreText = scoreFont.render('{0}'.format(score) , True, RED)


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

    if menu:
        tela_menu_inicial(window)
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu = False

    # ======= FALTA RECOMECAR ======
    elif menuPreta:
        tela_menu_preta(window)
        if event.type == pygame.MOUSEBUTTONDOWN:
            menuPreta = False

# ======= FALTA RECOMECAR & ARRUMAR CLICK ======
    # elif menuBranca:
    #     tela_menu_branca(window)
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         menuBranca = False


    else:
        # gerando linhas
        while len(all_notas) == 0 or (len(all_notas) < 5 and all_notas.sprites()[-1].rect.y > 0):
            x = random.randint(0, 3) * KEY_WIDTH
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
                    FPS += 1
                    
                    #Adicionando Score
                    score += 1
                    
                    certo = certo or True
                    sound_hits[sound_hit].play()
                    sound_hit = (sound_hit + 1) % len(sound_hits)
                    #Tocando música 

            if nota.rect.y >= 600 and nota.color=="Preto":
                print("errou")
                if score > highscore:
                    print('NEW HIGHSCORE')
                    highscore = score
                print('HIGHSCORE',highscore)
                sound_wrong.play()
                score = 0
                FPS = 60
                menuPreta = True
                
        if pos and not certo:
            if score > highscore:
                print('NEW HIGHSCORE')
                highscore = score
            print('HIGHSCORE', highscore)
            score = 0
            FPS = 60
            sound_wrong.play()
            menuBranca = True

        
        # ATUALIZA POSICAO
        all_sprites.update()
        

        window.fill((WHITE))

        all_sprites.draw(window)
        window.blit(scoreText, (250, 10))

    pygame.display.update()



pygame.quit()









