import pygame
import random
import time 

pygame.init()
pygame.font.init()


# =============== COR ===============
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
LIGHT_BLUE = (0, 255, 255)
GREY=(128,128,128)
SEMIRED=(255,125,125)
DARK_ORCHID=(104,34,139)


# =============== DISPLAY ===============
WIDTH = 500
HEIGHT = 600


# =============== NOTA ===============
KEY_WIDTH = 125
KEY_HEIGHT = 150
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TESTE")


# =============== CONTROLE DE VELOCIDADE ===============
clock=pygame.time.Clock()
FPS = 200
ACELERATION = 0.1
VELOCITY = 1

# =============== FONT ===============
font=pygame.font.SysFont('arial',45)
font_erro = pygame.font.SysFont('arial',30)
title=font.render("PIANO TILES",1,BLACK)
begin=font.render("Clique para iniciar!",1,BLUE)
textPERDEU=font_erro.render("PERDEU!.",1,WHITE)
textBRANCA=font_erro.render('VOCE APERTOU UMA NOTA BRANCA!',1,WHITE)
textPRETA=font_erro.render('VOCE PERDEU UMA NOTA PRETA!',1,WHITE)

# =============== VARIAVEIS ===============
game = True
score = 0
highscore = 0
menu = True
clicoubranca = False
perdeupreta = False



# =============== DEFINE NOTAS ===============
cor1 = BLACK
cor2 = BLACK
cor3 = BLACK
cor4 = BLACK
cor5 = BLACK

nota1x = 0 * KEY_WIDTH 
nota1y = -KEY_HEIGHT
nota2x = 1 * KEY_WIDTH 
nota2y = -KEY_HEIGHT
nota3x = 2 * KEY_WIDTH 
nota3y = -KEY_HEIGHT
nota4x = 3 * KEY_WIDTH 
nota4y = -KEY_HEIGHT
nota5x = 1 * KEY_WIDTH 
nota5y = -KEY_HEIGHT



# =============== JOGO ===============
while game:
    clock.tick(FPS)
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            menu = False
            
# =============== CLICK ===============
            posx, posy = pygame.mouse.get_pos()
            print('mouse ',posx, '         ',posy)
            print('nota', nota1x, '-', nota1x+KEY_WIDTH, '---',  nota1y, '-', nota1y+KEY_HEIGHT)
            
            if posx >= nota1x and posx <= nota1x + KEY_WIDTH and posy >= nota1y and posy <= nota1y + KEY_HEIGHT:
                cor1 = GREY
            if posx >= nota2x and posx <= nota2x + KEY_WIDTH and posy >= nota2y and posy <= nota2y + KEY_HEIGHT:
                cor2 = GREY
            else:
                print("\n ERROU \n")



# =============== MENU ===============
    if menu:
        if clicoubranca == False and perdeupreta == False:
            window.fill(GREY)
            titulotexto = title.get_rect()
            titulotexto.center=(250,200)
            window.blit(title,titulotexto)

            comecetexto = begin.get_rect()
            comecetexto.center = (250, 400)
            window.blit(begin,comecetexto)
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    menu = False
                    pygame.display.update()



# =============== LINHAS DIVISORIAS DE NOTAS ===============

    else:
        pygame.draw.line(window,BLACK,(KEY_WIDTH*1,0),(KEY_WIDTH*1,HEIGHT),1)
        pygame.draw.line(window,BLACK,(KEY_WIDTH*2,0),(KEY_WIDTH*2,HEIGHT),1)
        pygame.draw.line(window,BLACK,(KEY_WIDTH*3,0),(KEY_WIDTH*3,HEIGHT),1)

# =============== CRIA NOTAS ===============
        pygame.draw.rect(window,cor1,(nota1x,nota1y,KEY_WIDTH,KEY_HEIGHT))
        nota1y+=VELOCITY
        if nota1y>0:
            pygame.draw.rect(window,cor2,(nota2x,nota2y,KEY_WIDTH,KEY_HEIGHT))
            nota2y+=VELOCITY
            print(nota1y)
            print(nota1y)
        if nota2y>=0:
            pygame.draw.rect(window,cor3,(nota3x,nota3y,KEY_WIDTH,KEY_HEIGHT))
            nota3y+=VELOCITY
        if nota3y>=0:
            pygame.draw.rect(window,cor4,(nota4x,nota4y,KEY_WIDTH,KEY_HEIGHT))
            nota4y+=VELOCITY
        if nota4y>=0:
            pygame.draw.rect(window,cor5,(nota5x,nota5y,KEY_WIDTH,KEY_HEIGHT))
            nota5y+=VELOCITY

        if nota1y >= HEIGHT:
            # if cor1 == GREY:
            nota1x = 0 * KEY_WIDTH 
            nota1y = -KEY_HEIGHT
            cor1 = BLACK
            # else:
            #     menu = True
        if nota2y >= HEIGHT:
            # if cor2 == GREY:
            nota2x = 1 * KEY_WIDTH 
            nota2y = -KEY_HEIGHT
            cor2 = BLACK
            # else:
            #     menu = True
        elif nota3y >= HEIGHT:
            nota3x = 2 * KEY_WIDTH 
            nota3y = -KEY_HEIGHT
            cor3 = BLACK
        elif nota4y >= HEIGHT:
            nota4x = 3 * KEY_WIDTH 
            nota4y = -KEY_HEIGHT
            cor4 = BLACK
        elif nota5y >= HEIGHT:
            nota5x = 1 * KEY_WIDTH 
            nota5y = -KEY_HEIGHT
            cor5 = BLACK

# =============== CLICOU EM BRANCA ===============




# =============== PERDEU PRETA ===============




# =============== ATUALIZAR ===============
    pygame.display.update()
pygame.quit()






# =============== CORRECOES FUTURAS ===============
    # DEPOIS QUE ARRUMAR AS CORES, MUDAR PARA ISSO
        # if nota1y > HEIGHT:
        #     if cor1 == BLACK:
        #         nota1x = random.randint(0,3) * KEY_WIDTH 
        #         nota1y = -KEY_HEIGHT
        #     else:
        #         game = False




# CNTRL X 
# if event.type == pygame.MOUSEBUTTONUP:
#             pass