'''
   JOGO PYGAME USANDO UDP
ALIX SANCHES        42133017
AMANDA SMANIOTO     42127351
LAURA ABI DAUD      42118816
'''

import pygame
import random

pygame.display.init()
pygame.mixer.init()

# DEFININDO TAMANHO DA TELA
x = 800
y = 650

# MUSICA DE FUNDO
#pygame.mixer.music.load("GAME/Assets/Cats_on_Mars.mp3")
#pygame.mixer.music.play(-1) # -1 FICA REPETINDO A MUSICA 

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('ATV DE REDES - JOGO')

background = pygame.image.load('GAME/Assets/fundo3.png').convert_alpha()
background = pygame.transform.scale(background, (x,y))

meteoro = pygame.image.load('GAME/Assets/meteoro.png').convert_alpha()
meteoro = pygame.transform.scale(meteoro, (45,45))
pos_meteoro = [750,200]

# JOGADOR FOGUETE 1
foguete1 = pygame.image.load('GAME/Assets/foguete1.png').convert_alpha()
foguete1 = pygame.transform.scale(foguete1, (60,60))
foguete1 = pygame.transform.rotate(foguete1, -90) # GIRA A NAVE EM 90 GAUS 
pos_foguete1 = [10,100] # POSICA DO FOGUETE 

# JOGADOR FOGUETE 2
foguete2 = pygame.image.load('GAME/Assets/foguete2.png').convert_alpha()
foguete2 = pygame.transform.scale(foguete2, (60,60))
foguete2 = pygame.transform.rotate(foguete2, -90) # GIRA A NAVE EM 90 GAUS
pos_foguete2 = [10,500] # POSICAO DO FOGUETE 2

# MISSILS
missilV1 = pygame.image.load('GAME/Assets/missilVerde1.png').convert_alpha()
missilV1 = pygame.transform.scale(missilV1, (25,25))
missilV1 = pygame.transform.rotate(missilV1, -90)
pos_missilV1 = pos_foguete1 # POSICAO DO MISSIL 1 DO FOGUETE 1
vel_missilV1 = 0; 

missilV2 = pygame.image.load('GAME/Assets/missilVerde2.png').convert_alpha()
missilV2 = pygame.transform.scale(missilV2, (25,25))
missilV2 = pygame.transform.rotate(missilV2, -90)
pos_missilV2 = pos_foguete2 # POSICAO DO MISSIL 2 DO FOGUETE 2
vel_missilV2 = 0; 

# PARA FAZER A COLISAO TEMOS QUE TRANSFORMAR IMAGEM EM OBJETOS 
# A FUNCAO GET_RECT() TRANSFORMA AS IMAMGENS EM OBJETOS     
foguete_rect =  foguete1.get_rect()
foguete2_rect = foguete2.get_rect()
missilV1_rect = missilV1.get_rect()
missilV2_rect = missilV2.get_rect()
meteoro_rect =  meteoro.get_rect()

def respawn_meteoro():
    x = 850
    y = random.randint(1, 460)
    return [x,y]

def respawn_missilV1():
    tiro1 = False 
    respawn_missilV1 = pos_foguete1
    vel_missilV1 = 0
    return [respawn_missilV1, tiro1, vel_missilV1]

def respawn_missilV2():
    tiro2 = False 
    respawn_missilV2 = pos_foguete2
    vel_missilV2 = 0
    return [respawn_missilV2, tiro2, vel_missilV2]

score = 5
def colisoes():
    global score
    if pos_foguete1 == 0:
        return True
    else: 
        return False 

# WHILE PARA RODAR O JOGO E NAO FECHAR 
tiro1 = False
tiro2 = False
app_rodando = True

while app_rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_rodando = False
            flag_game = False
    
    screen.blit(background, (0,0))
    
    rel_x = x % background.get_rect().width
    screen.blit(background, (rel_x - background.get_rect().width,0))
    if rel_x < 800:
        screen.blit(background, (rel_x, 0))

    # TECLAS PARA PODER MEXER OS FOGUETES
    tecla = pygame.key.get_pressed()
    # FOGUETE 1 (ROSA)
    if tecla[pygame.K_a] and pos_foguete1[0] > 1:
        pos_foguete1[0] -= 1
        if not tiro1:
            pos_missilV1[0] -= 1
    if tecla[pygame.K_d] and pos_foguete1[0] < 740:
        pos_foguete1[0] += 1
        if not tiro1:
            pos_missilV1[0] += 1
    if tecla[pygame.K_w] and pos_foguete1[1] > 1:
        pos_foguete1[1] -= 1
        if not tiro1:
            pos_missilV1[1] -= 1
    if tecla[pygame.K_s] and pos_foguete1[1] < 600:
        pos_foguete1[1] += 1
        if not tiro1:
            pos_missilV1[1] += 1

    # FOGUETE 2 (AMARELO)
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_foguete2[1] > 1:
        pos_foguete2[1] -= 1
        if not tiro2:
            pos_missilV2[1] -= 1
    if tecla[pygame.K_DOWN] and pos_foguete2[1] < 600:
        pos_foguete2[1] += 1
        if not tiro2:
            pos_missilV2[1] += 1
    if tecla[pygame.K_LEFT] and pos_foguete2[0]> 1:
        pos_foguete2[0] -= 1
        if not tiro2:
            pos_missilV2[0] -= 1
    if tecla[pygame.K_RIGHT] and pos_foguete2[0] < 740:
        pos_foguete2[0] += 1
        if not tiro2:
            pos_missilV2[0] += 1

    # TIRO MISSIL 1
    if tecla[pygame.K_SPACE]:
        tiro1 = True
        vel_missilV1 = 2
    # TIRO MISSIL 2
    if tecla[pygame.K_m]:
        tiro2 = True
        vel_missilV2 = 2

    # POSICAO RECT
    foguete_rect.y =  pos_foguete1[1]
    foguete_rect.x =  pos_foguete1[0]
    foguete2_rect.y = pos_foguete2[1]
    foguete2_rect.x = pos_foguete2[0]

    missilV1_rect.x = pos_missilV1[0]
    missilV1_rect.y = pos_missilV1[1]
    missilV2_rect.x = pos_missilV2[0]
    missilV2_rect.y = pos_missilV2[1]

    meteoro_rect.x = pos_meteoro[0]
    meteoro_rect.y = pos_meteoro[1]

    # MOVIMENTOS
    x -= 0.7
    pos_meteoro[0] -= 2
    
    # RESPAWN DOS MISSEIS 
    pos_missilV1[0] += vel_missilV1
    if pos_missilV1[0] >= 800:
        pos_missilV1, tiro1, vel_missilV1 = respawn_missilV1()

    pos_missilV2[0] += vel_missilV2
    if pos_missilV2[0] >= 800:
        pos_missilV2, tiro2, vel_missilV2 = respawn_missilV2()

    # DESENHA EM VOLTA DOS OBJETOS 
    pygame.draw.rect(screen, (255, 0, 0), foguete_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), foguete2_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), missilV1_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), missilV2_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), meteoro_rect, 4)

    # RESPAWN METEOROS
    if pos_meteoro[0] <= -100 or colisoes():
        pos_meteoro = respawn_meteoro()

    # CRIA IMAGENS DOS DOIS MISSEIS 
    # COLOQUEI O SCREEN BLIT DOS MISSEIS ANTES DOS FOGUETES PARA NAO SOBREPOR OS FOGUETES
    screen.blit(missilV1, (pos_missilV1[0], pos_missilV1[1]))
    screen.blit(missilV2, (pos_missilV2[0], pos_missilV2[1]))
    # CRIA IMAGENS DOS DOIS FOGUETES
    screen.blit(foguete1, (pos_foguete1[0], pos_foguete1[1]))
    screen.blit(foguete2, (pos_foguete2[0], pos_foguete2[1]))
    # CRIA A IMAGEM DO METEORO
    screen.blit(meteoro, (pos_meteoro[0], pos_meteoro[1]))

    pygame.display.update()

pygame.display.quit()



