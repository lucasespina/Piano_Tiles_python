# Imports 
import pygame
from pygame import mixer
import random
import time 
from Assets.classes import Nota
from Assets.initial_settings import *

# Inicialização 
pygame.init()


#Definindo as fontes
font = pygame.font.SysFont(None,48)
scoreFont = pygame.font.SysFont(None, 40)

#Highscore inicial
highscore = 0

# 
while game:

    pos = None
    clock.tick(FPS)

    #Texto do score formtado
    scoreText = scoreFont.render('{0}'.format(score) , True, RED)

    # EVENTOS
    for event in pygame.event.get():
        # EXIT
        if event.type == pygame.QUIT:
            game = False
        
        # Mouse Posição Click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
        #Restart o game ápos perder
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                    menuPreta = False  
        
        
    #Menu inicial
    if menu_inicial:
        tela_menu_inicial(window)
        if not play_one:
            sound_menu.play(loops=-1)
            play_one = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound_menu.stop()
            menu_inicial = False

    # Tela de erro
    elif menuPreta:
        tela_menu_preta(window,highscore)
        
        
        #Restaurando as condições inicias ápos perde
        pos = None
        score = 0
        
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


    # Começando o jogo
    else:
        
        highscore = 0 
        
        #Gerando as notas
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

                   #Tocando nota
                   if nota.color=="Preto":

                        #Som da tecla
                        numeroNota = random.randint(0,len(listaSound)-1)
                        listaSound[numeroNota].play()

                        #Mudando a cor da tecla clicada
                        nota.img(nota_img_clicada, nota.rect.x, nota.rect.y)

                        #Aumentando a velocidade após clicar
                        FPS += 1
                        
                        #Adicionando Score
                        score += 1
                    
                        # Conferindo posição certa
                        certo = certo or True
                    
            # Erros da nota preta que passou
            if nota.rect.y >= 600 and nota.color=="Preto":
                if score > highscore:
                    highscore = score
                
                menuPreta = True
                
                # Som de errado
                sound_wrong.play()

        # Erros de nota não preta   
        if pos and not certo:
            
            if score > highscore:
                highscore = score
            
            # Ligando o menu
            menuPreta = True
            
            # Som de errado
            sound_wrong.play()
        
        # ATUALIZA POSICAO
        all_sprites.update()
        
        # Desenhando tela de jogo
        window.fill((WHITE))
        all_sprites.draw(window)
        #Desenhando linhas
        pygame.draw.line(window,BLACK,(KEY_WIDTH*1,0),(KEY_WIDTH*1,HEIGHT),1)
        pygame.draw.line(window,BLACK,(KEY_WIDTH*2,0),(KEY_WIDTH*2,HEIGHT),1)
        pygame.draw.line(window,BLACK,(KEY_WIDTH*3,0),(KEY_WIDTH*3,HEIGHT),1)
        
        
        mx , my = pygame.mouse.get_pos()
        particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
        
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            pygame.draw.circle(window, (255, 0, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)
            

        #Score Text
        window.blit(scoreText, (250, 10))

    pygame.display.update()

pygame.quit()









