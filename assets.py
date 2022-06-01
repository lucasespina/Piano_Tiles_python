
import pygame

# ------------------ DADOS -----------------------------

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

# DISPLAY
WIDTH = 500
HEIGHT = 600
# ASSETS
KEY_WIDTH = 125
KEY_HEIGHT = 150
window = pygame.display.set_mode((KEY_WIDTH*4,HEIGHT))
pygame.display.set_caption("Insper Music")
nota_img = pygame.image.load('Tecla.png').convert_alpha()
nota_img = pygame.transform.scale(nota_img, (KEY_WIDTH, KEY_HEIGHT))
nota_img_clicada = pygame.image.load('teclaclicada.png').convert_alpha()
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
# all_black = pygame.sprite.Group()
# all_white = pygame.sprite.Group()
# all_gray = pygame.sprite.Group()

all_notas = pygame.sprite.Group()

# MENU
pygame.font.init()
font=pygame.font.SysFont('arial',45)
font_erro = pygame.font.SysFont('arial',30)

title=font.render("PIANO TILES",1,BLACK)
begin=font.render("Clique para iniciar!",1,BLUE)
textPERDEU=font_erro.render("PERDEU!!!",1,WHITE)
textBRANCA=font_erro.render('VOCE APERTOU UMA NOTA BRANCA!',1,WHITE)
textPRETA=font_erro.render('VOCE PERDEU UMA NOTA PRETA!',1,WHITE)

def tela_menu_inicial(tela):
    clock = pygame.time.Clock()
    # FUNDO 
    tela.fill(GREY)
    titulotexto = title.get_rect()
    titulotexto.center=(250,200)
    tela.blit(title,titulotexto)
    comecetexto = begin.get_rect()
    comecetexto.center = (250, 400)
    tela.blit(begin,comecetexto)
    
    return None

def tela_menu_preta(tela):
    clock = pygame.time.Clock()
    # FUNDO 
    tela.fill(GREY)
    perdeutexto = textPERDEU.get_rect()
    perdeutexto.center=(250,200)
    tela.blit(textPERDEU,perdeutexto)
    pretatexto = textPRETA.get_rect()
    pretatexto.center = (250, 400)
    tela.blit(textPRETA,pretatexto)
    
    return None


def tela_menu_branca(tela):
    clock = pygame.time.Clock()
    # FUNDO 
    tela.fill(GREY)
    perdeutexto = textPERDEU.get_rect()
    perdeutexto.center=(250,200)
    tela.blit(textPERDEU,perdeutexto)
    brancatexto = textBRANCA.get_rect()
    brancatexto.center = (250, 400)
    tela.blit(textBRANCA,brancatexto)
    
    return None

# pygame.mixer.init()
# sound = pygame.mixer
# def som (musica):
#     pygame.mixer.music.load(musica)
#     pygame.mixer.music.set_volume(0.7)
    
#     start = 0.2
#                     end = 0.4
#                     def play(sound, start, end):
#                         sound.set_pos(start)
#                         sound.play()
#                         time.sleep(end - start)     # in seconds
#                         sound.stop()

