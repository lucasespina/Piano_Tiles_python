# Imports 
import pygame
from pygame import mixer
import random
import time 
from Assets.classes import Nota
from Assets.initial_configs import *

# Inicialização 
pygame.init()
font = pygame.font.SysFont(None,48)
scoreFont = pygame.font.SysFont(None, 40)

pos = None

# Variaveis
game = True
menu_inicial = True
menuPreta = False
menuBranca = False
score = 0
highscore = 0

# Definindo sons
mixer.init()
mixer.music.set_volume(0.07)

# Rodando o Jogo
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
        
        # Mouse Posição Click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
    if menu_inicial:
        tela_menu_inicial(window)
        if event.type == pygame.MOUSEBUTTONDOWN:
           menu_inicial = False

    # ======= FALTA RECOMECAR ======
    elif menuPreta:
        tela_menu_preta(window)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = None
            score = 0
            highscore = 0
            
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

            # CONTROLE DE VELOCIDADE
            clock = pygame.time.Clock()
            FPS = 60
            velocity = 15
            aceleration = 1

        # GRUPOS
            all_sprites = pygame.sprite.Group()
            all_notas = pygame.sprite.Group()

            menuPreta = False

    else:
        # gerando linhas
        while len(all_notas) == 0 or (len(all_notas) < 5 and all_notas.sprites()[-1].rect.y > 0):
            x = random.randint(0, 3) * KEY_WIDTH
            # x = KEY_WIDTH
            y = -KEY_HEIGHT
            n = Nota(nota_img, x, y)
            all_notas.add(n)
            all_sprites.add(n)

        
        #Tecla Clicada
        certo = False
        for nota in all_notas:
            if pos:
                if nota.rect.collidepoint(pos):

                   # Tocando a nota, ao acertar a posição
                   
                   if nota.color=="Preto":
                   
                        numeroNota = random.randint(0,len(listaSound)-1)
                        listaSound[numeroNota].play()

                    #Mudando a cor da tecla clicada
                        nota.img(nota_img_clicada, nota.rect.x, nota.rect.y)

                        #Aumentando a velocidade após clicar
                        FPS += 1
                        
                        #Adicionando Score
                        score += 1
                        
                        certo = certo or True
                    
            # Erros da nota preta que passou
            if nota.rect.y >= 600 and nota.color=="Preto":
                print("errou")
                if score > highscore:
                    print('NEW HIGHSCORE')
                    highscore = score
                print('HIGHSCORE',highscore)
                # Som de errado
                sound_wrong.play()
                
                score = 0
                FPS = 60
                
                menuPreta = True

        # Erros de nota não preta   
        if pos and not certo:
            if score > highscore:
                print('NEW HIGHSCORE')
                highscore = score
            print('HIGHSCORE', highscore)
            
            score = 0
            FPS = 60
            # Som de errado
            
            sound_wrong.play()
            
            menuBranca = True

        # ATUALIZA POSICAO
        all_sprites.update()
        

        window.fill((WHITE))

        all_sprites.draw(window)
        window.blit(scoreText, (250, 10))

    pygame.display.update()



pygame.quit()









