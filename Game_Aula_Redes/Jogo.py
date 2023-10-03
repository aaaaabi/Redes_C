'''
   JOGO PYGAME USANDO UDP
ALIX SANCHES        42133017
AMANDA SMANIOTO     42127351
LAURA ABI DAUD      42118816
'''

import pygame
import random
import time
#from random import*
#from PIL import Image, ImageDraw 

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

bg = pygame.image.load('GAME/Assets/fundo3.png').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

meteoro = pygame.image.load('GAME/Assets/meteoro.png').convert_alpha()
meteoro = pygame.transform.scale(meteoro, (45,45))
pos_met_x = 750; pos_met_y = 200

#meteoro2 = pygame.image.load('GAME/Assets/meteoro.png').convert_alpha()
#meteoro2 = pygame.transform.scale(meteoro2, (45,45))
#pos_met2_x = 750; pos_met2_y = 400

# JOGADOR FOGUETE 1
foguete = pygame.image.load('GAME/Assets/foguete1.png').convert_alpha()
foguete = pygame.transform.scale(foguete, (60,60))
foguete = pygame.transform.rotate(foguete, -90) # GIRA A NAVE EM 90 GAUS 
pos_fogute_x = 10; pos_fogute_y = 100 # POSICA DO FOGUETE 

# JOGADOR FOGUETE 2
foguete2 = pygame.image.load('GAME/Assets/foguete2.png').convert_alpha()
foguete2 = pygame.transform.scale(foguete2, (50,50))
foguete2 = pygame.transform.rotate(foguete2, -90) # GIRA A NAVE EM 90 GAUS
pos_fogute2_x = 10; pos_fogute2_y = 500 # POSICAO DO FOGUETE 2

# MISSILS
missilV1 = pygame.image.load('GAME/Assets/missilVerde1.png').convert_alpha()
missilV1 = pygame.transform.scale(missilV1, (25,25))
missilV1 = pygame.transform.rotate(missilV1, -90)
pos_missilV1_x = pos_fogute_x; pos_missilV1_y = pos_fogute_y # POSICAO DO MISSIL 1 DO FOGUETE 1
vel_missilV1 = 0; 

missilV2 = pygame.image.load('GAME/Assets/missilVerde2.png').convert_alpha()
missilV2 = pygame.transform.scale(missilV2, (25,25))
missilV2 = pygame.transform.rotate(missilV2, -90)
pos_missilV2_x = pos_fogute2_x; pos_missilV2_y = pos_fogute2_y # POSICAO DO MISSIL 2 DO FOGUETE 2
vel_missilV2 = 0; 

def respawn_meteoro():
    x = 850
    y = random.randint(1, 460)
    return [x,y]
    #meteoro_respawn_time = random.randit(1,200)
    #return [x,y,meteoro_respawn_time]

def respawn_missilV1():
    tiro1 = False 
    respawn_missilV1_x = pos_fogute_x
    respawn_missilV1_y = pos_fogute_y
    vel_missilV1 = 0
    return [respawn_missilV1_x, respawn_missilV1_y, tiro1, vel_missilV1]

def respawn_missilV2():
    tiro2 = False 
    respawn_missilV2_x = pos_fogute2_x
    respawn_missilV2_y = pos_fogute2_y
    vel_missilV2 = 0
    return [respawn_missilV2_x, respawn_missilV2_y, tiro2, vel_missilV2]

# WHILE PARA RODAR O JOGO E NAO FECHAR 
tiro1 = False
tiro2 = False
rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            flag_game = False
    screen.blit(bg, (0,0))
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 800:
        screen.blit(bg, (rel_x, 0))

    # TECLAS PARA PODER MEXER OS FOGUETES
    # FOGUETE 2 (AMARELO)
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_fogute2_y > 1:
        pos_fogute2_y -= 1
        if not tiro2:
            pos_missilV2_y -= 1
    if tecla[pygame.K_DOWN] and pos_fogute2_y < 605:
        pos_fogute2_y += 1
        if not tiro2:
            pos_missilV2_y += 1
    if tecla[pygame.K_LEFT] and pos_fogute2_x > 1:
        pos_fogute2_x -= 1
        if not tiro2:
            pos_missilV2_x -= 1
    if tecla[pygame.K_RIGHT] and pos_fogute2_x < 750:
        pos_fogute2_x += 1
        if not tiro2:
            pos_missilV2_x += 1
    
    # FOGUETE 1 (ROSA)
    if tecla[pygame.K_a] and pos_fogute_x > 1:
        pos_fogute_x -= 1
        if not tiro1:
            pos_missilV1_x -= 1
    if tecla[pygame.K_d] and pos_fogute_x < 740:
        pos_fogute_x += 1
        if not tiro1:
            pos_missilV1_x += 1
    if tecla[pygame.K_w] and pos_fogute_y > 1:
        pos_fogute_y -= 1
        if not tiro1:
            pos_missilV1_y -= 1
    if tecla[pygame.K_s] and pos_fogute_y < 600:
        pos_fogute_y += 1
        if not tiro1:
            pos_missilV1_y += 1

    # TIRO MISSIL 1
    if tecla[pygame.K_SPACE]:
        tiro1 = True
        vel_missilV1 = 2

    # TIRO MISSIL 2
    if tecla[pygame.K_m]:
        tiro2 = True
        vel_missilV2 = 2

    # MOVIMENTOS
    x -= 0.7
    pos_met_x -= 2
    #pos_met2_x -= 2
    pos_missilV1_x += vel_missilV1
    if pos_missilV1_x >= 800:
            pos_missilV1_x, pos_missilV1_y, tiro1, vel_missilV1 = respawn_missilV1()

    pos_missilV2_x += vel_missilV2
    if pos_missilV2_x >= 800:
        pos_missilV2_x, pos_missilV2_y, tiro2, vel_missilV2 = respawn_missilV2()

    # RESPAWN METEOROS
    if pos_met_x <= -100:
        pos_met_x = respawn_meteoro()[0]
        pos_met_y = respawn_meteoro()[1]
    
    # CRIA IMAGENS DOS DOIS MISSEIS 
    # COLOQUEI O SCREEN BLIT DOS MISSEIS ANTES DOS FOGUETES PARA NAO SOBREPOR OS FOGUETES
    screen.blit(missilV1, (pos_missilV1_x, pos_missilV1_y))
    screen.blit(missilV2, (pos_missilV2_x, pos_missilV2_y))
    # CRIA IMAGENS DOS DOIS FOGUETES
    screen.blit(foguete, (pos_fogute_x, pos_fogute_y))
    screen.blit(foguete2, (pos_fogute2_x, pos_fogute2_y))
    screen.blit(meteoro, (pos_met_x, pos_met_y))
    #screen.blit(meteoro2, (pos_met2_x, pos_met2_y))

    pygame.display.update()

pygame.display.quit()

# TO DO 
# 1.0 ARRUMAR O RESPAWN DOS MISSEIS, ELES NAO FUNCIONAM
# 2.0 COLOCAR OS METEOROS ALEATORIOS 
# 3.0 FAZER A COLISAO: 
    # 3.1 FAZER COM QUE SE OS FOGUETES SE COLIDIREM DESCONTA UM PONTO ATE MORREREM
    # 3.2 SE UM DOS MISSESIS ATINGIR O FOGUETE DESCONTA UM PONTO ATE MORREREM 
    # 3.3 SE UM DOS FOGUETES ENCOSTAR NO METEORO DESCONTA UM PONTO ATE MORREREM 