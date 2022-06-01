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

# Definindo sons
mixer.init()
mixer.music.set_volume(0.02)
# Som de tecla errada
sound_wrong = pygame.mixer.Sound('wrong.wav')
# Sons de melodia para teclas certas
soundA = pygame.mixer.Sound('piano_A.wav')
soundB = pygame.mixer.Sound('piano_B.wav')
soundC = pygame.mixer.Sound('piano_C.wav')
soundD = pygame.mixer.Sound('piano_D.wav')
soundE = pygame.mixer.Sound('piano_E.wav')
soundF = pygame.mixer.Sound('piano_F.wav')
soundG = pygame.mixer.Sound('piano_G.wav')

listaSound = [soundA, soundB, soundC, soundD, soundE, soundF, soundG]

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

                   
                    numeroNota = random.randint(0,len(listaSound)-1)
                    listaSound[numeroNota].play()

                    #Mudando a cor da tecla clicada
                    nota.img(nota_img_clicada, nota.rect.x, nota.rect.y)
                    

                    #Aumentando a velocidade após clicar
                    FPS += 1
                    
                    #Adicionando Score
                    score += 1
                    
                    certo = certo or True
                    

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









