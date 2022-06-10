
import pygame
from pygame import mixer
# ------------------ DADOS -----------------------------

#First Display Config

pos = None
play_one = False
game = True
menu_inicial = True
menuPreta = False
menuBranca = False
score = 0
# highscore = 0

# Definindo sons
mixer.init()
mixer.music.set_volume(10)

#Particulas
particles = []





# CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
LIGHT_BLUE = (0, 255, 255)
GREY = (152,152,152)

# lista cor efeito especial
c_lista = [WHITE, BLACK, RED, GREY]

pygame.mixer.init()

sound_menu = pygame.mixer.Sound('Sounds/menu.wav')
# Som de tecla errada
sound_wrong = pygame.mixer.Sound('Sounds/wrong.wav')
# Sons de melodia para teclas certas
soundA = pygame.mixer.Sound('Sounds/piano_A.wav')
soundB = pygame.mixer.Sound('Sounds/piano_B.wav')
soundC = pygame.mixer.Sound('Sounds/piano_C.wav')
soundD = pygame.mixer.Sound('Sounds/piano_D.wav')
soundE = pygame.mixer.Sound('Sounds/piano_E.wav')
soundF = pygame.mixer.Sound('Sounds/piano_F.wav')
soundG = pygame.mixer.Sound('Sounds/piano_G.wav')
# Lista de sons para notas
listaSound = [soundA, soundB, soundC, soundD, soundE, soundF, soundG]

# DISPLAY
WIDTH = 500
HEIGHT = 600
# ASSETS
KEY_WIDTH = 125
KEY_HEIGHT = 150
window = pygame.display.set_mode((KEY_WIDTH*4,HEIGHT))
pygame.display.set_caption("Insper Music")

#Imagens usadas no jogo
pygame.display.set_icon(pygame.image.load('Images/icone.png'))
nota_img = pygame.image.load('Images/Tecla.png').convert_alpha()
nota_img = pygame.transform.scale(nota_img, (KEY_WIDTH, KEY_HEIGHT))
nota_img_clicada = pygame.image.load('Images/teclaclicada.png').convert_alpha()
nota_img_clicada = pygame.transform.scale(nota_img_clicada, (KEY_WIDTH, KEY_HEIGHT))


#nota = pygame.draw.rect(window,(BLACK),(x1,y,KEY_WIDTH,KEY_HEIGHT))

# Width, Height das notas
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

# MENU

background_image = pygame.image.load('Images/Fundo.png')
lose_image = pygame.image.load('Images/lose.png')


#Função do menu inicial
def tela_menu_inicial(tela):
    
    # FUNDO 
    tela.blit(background_image, (0,0))
    
    return None

#Função da tela de derrota
def tela_menu_preta(tela,highscore):
    
    tela.blit(lose_image, (0,0))
    highscoreFont = pygame.font.SysFont(None, 120)
    highscoretxt = highscoreFont.render('{0}'.format(highscore) , True, RED)
    
    if highscore >= 10:
        tela.blit(highscoretxt, (205, 200))
    if highscore < 10 :
        tela.blit(highscoretxt, (230, 200))
        
    return None


