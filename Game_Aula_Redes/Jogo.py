import pygame
from random import*
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

# JOGADOR FOGUETE 1
foguete = pygame.image.load('GAME/Assets/foguete1.png').convert_alpha()
foguete = pygame.transform.scale(foguete, (60,60))
foguete = pygame.transform.rotate(foguete, -90) # GIRA A NAVE EM 90 GAUS 
pos_fogute_x = 100; pos_fogute_y = 10 # POSICA DO FOGUETE 

# JOGADOR FOGUETE 2
foguete2 = pygame.image.load('GAME/Assets/foguete2.png').convert_alpha()
foguete2 = pygame.transform.scale(foguete2, (50,50))
foguete2 = pygame.transform.rotate(foguete2, -90) # GIRA A NAVE EM 90 GAUS
pos_fogute2_x = 10; pos_fogute2_y = 500 # POSICAO DO FOGUETE 2

# MISSILS
missilV1 = pygame.image.load('GAME/Assets/missilVerde1.png').convert_alpha()
missilV1 = pygame.transform.scale(missilV1, (25,25))
missilV1 = pygame.transform.rotate(missilV1, -90)
pos_missilV1_x = 117; pos_missilV1_y = 25 # POSICAO DO MISSIL 1 DO FOGUETE 1
vel_missilV1 = 0; 

missilV2 = pygame.image.load('GAME/Assets/missilVerde2.png').convert_alpha()
missilV2 = pygame.transform.scale(missilV2, (25,25))
missilV2 = pygame.transform.rotate(missilV2, -90)
pos_missilV2_x = 20; pos_missilV2_y = 513 # POSICAO DO MISSIL 2 DO FOGUETE 2
vel_missilV2 = 0; 

meteoro = pygame.image.load('GAME/Assets/meteoro.png').convert_alpha()
meteoro = pygame.transform.scale(meteoro, (30,30))
met_x = 30; met_y = 60
 
def respawn_missilV1():
    triggered1 = False 
    respawn_missilV1_x = pos_fogute_x
    respawn_missilV1_y = pos_fogute_y
    vel_missilV1 = 0
    return [respawn_missilV1_x, respawn_missilV1_y, triggered1, vel_missilV1]

def respawn_missilV2():
    triggered2 = False 
    respawn_missilV2_x = pos_fogute_x
    respawn_missilV2_y = pos_fogute_y
    vel_missilV2 = 0
    return [respawn_missilV2_x, respawn_missilV2_y, triggered2, vel_missilV2]

# WHILE PARA RODAR O JOGO E NAO FECHAR 
triggered1 = False
triggered2 = False
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))
    screen.blit(meteoro, (met_x, met_y))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 800:
        screen.blit(bg, (rel_x, 0))

    # TECLAS PARA PODER MEXER OS FOGUETES
    # FOGUETE 2 (AMARELO)
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_fogute2_y > 1:
        pos_fogute2_y -= 1
        if not triggered2:
            pos_missilV2_y -= 1
    if tecla[pygame.K_DOWN] and pos_fogute2_y < 605:
        pos_fogute2_y += 1
        if not triggered2:
            pos_missilV2_y += 1
    if tecla[pygame.K_LEFT] and pos_fogute2_x > 1:
        pos_fogute2_x -= 1
        if not triggered2:
            pos_missilV2_x -= 1
    if tecla[pygame.K_RIGHT] and pos_fogute2_x < 750:
        pos_fogute2_x += 1
        if not triggered2:
            pos_missilV2_x += 1
    
    # FOGUETE 1 (ROSA)
    if tecla[pygame.K_a] and pos_fogute_y > 1:
        pos_fogute_y -= 1
        if not triggered1:
            pos_missilV1_y -= 1
    if tecla[pygame.K_d] and pos_fogute_y < 740:
        pos_fogute_y += 1
        if not triggered1:
            pos_missilV1_y += 1
    if tecla[pygame.K_w] and pos_fogute_x > 1:
        pos_fogute_x -= 1
        if not triggered1:
            pos_missilV1_x -= 1
    if tecla[pygame.K_s] and pos_fogute_x < 600:
        pos_fogute_x += 1
        if not triggered1:
            pos_missilV1_x += 1

    # TIRO MISSIL 1
    if tecla[pygame.K_SPACE]:
        triggered1 = True
        vel_missilV1 = 2
    # TIRO MISSIL 2
    if tecla[pygame.K_m]:
        triggered2 = True
        vel_missilV2 = 2

    # RESPAWN MISSIL DO FOGUETE 1 
    if pos_missilV1_y == 100:
        pos_missilV1_x, pos_missilV1_y, triggered1, vel_missilV1 = respawn_missilV1()
    # RESPAWN MISSIL DO FOGUETE 2
    if pos_missilV2_y == 100:
        pos_missilV2_x, pos_missilV2_y, triggered2, vel_missilV2 = respawn_missilV2()

    # MOVIMENTO DO FUNDO
    x -= 0.7
    pos_missilV1_y += vel_missilV1
    pos_missilV2_x += vel_missilV2
    
    # CRIA IMAGENS DOS DOIS MISSEIS 
    # COLOQUEI O SCREEN BLIT DOS MISSEIS ANTES DOS FOGUETES PARA NAO SOBREPOR OS FOGUETES
    screen.blit(missilV1, (pos_missilV1_y, pos_missilV1_x))
    screen.blit(missilV2, (pos_missilV2_x, pos_missilV2_y))
    # CRIA IMAGENS DOS DOIS FOGUETES
    screen.blit(foguete, (pos_fogute_y, pos_fogute_x))
    screen.blit(foguete2, (pos_fogute2_x, pos_fogute2_y))

    pygame.display.update()

pygame.display.quit()

# TO DO 
# 1.0 ARRUMAR O RESPAWN DOS MISSEIS, ELES NAO FUNCIONAM
# 2.0 COLOCAR OS METEOROS ALEATORIOS 
# 3.0 FAZER A COLISAO: 
    # 3.1 FAZER COM QUE SE OS FOGUETES SE COLIDIREM DESCONTA UM PONTO ATE MORREREM
    # 3.2 SE UM DOS MISSESIS ATINGIR O FOGUETE DESCONTA UM PONTO ATE MORREREM 
    # 3.3 SE UM DOS FOGUETES ENCOSTAR NO METEORO DESCONTA UM PONTO ATE MORREREM 