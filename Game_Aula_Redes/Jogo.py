'''
   JOGO PYGAME USANDO UDP
ALIX SANCHES        42133017
AMANDA SMANIOTO     42127351
LAURA ABI DAUD      42118816
'''

import pygame
from random import*
#pygame.RESIZABLE
pygame.display.init()
pygame.mixer.init()

# DEFININDO TAMANHO DA TELA
x = 800
y = 650

# TELA CHEIA
#display_info = pygame.display.Info()
#screen = pygame.display.set_mode((display_info.current_w, display_info.current_h-60), pygame.RESIZABLE)

# MUSICA DE FUNDO
#pygame.mixer.music.load("GAME/Assets/Cats_on_Mars.mp3")
#pygame.mixer.music.play(-1) # -1 FICA REPETINDO A MUSICA 

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Teste')

bg = pygame.image.load('Game_Aula_Redes/GAME/Assets/fundo3.png').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

meteoro = pygame.image.load('Game_Aula_Redes/GAME/Assets/meteoro.png').convert_alpha()
meteoro = pygame.transform.scale(meteoro, (45,45))
pos_met_x = 750; pos_met_y = 200

#meteoro2 = pygame.image.load('GAME/Assets/meteoro.png').convert_alpha()
#meteoro2 = pygame.transform.scale(meteoro2, (45,45))
#pos_met2_x = 750; pos_met2_y = 400

# JOGADOR FOGUETE 1
foguete = pygame.image.load('Game_Aula_Redes/GAME/Assets/foguete1.png').convert_alpha()
foguete = pygame.transform.scale(foguete, (60,60))
foguete = pygame.transform.rotate(foguete, -90) # GIRA A NAVE EM 90 GAUS 
# POSICA DO FOGUETE 
pos_fogute_x = 100; pos_fogute_y = 10

# JOGADOR FOGUETE 2
foguete2 = pygame.image.load('Game_Aula_Redes/GAME/Assets/foguete2.png').convert_alpha()
foguete2 = pygame.transform.scale(foguete2, (50,50))
foguete2 = pygame.transform.rotate(foguete2, -90) # GIRA A NAVE EM 90 GAUS
# POSICAO DO FOGUETE 2
pos_fogute2_x = 10; pos_fogute2_y = 500

#meteoro = foguete = pygame.image.load('GAME/Assets/meteoro.png').convert_alpha()
#meteoro = pygame.transform.scale(meteoro, (0,0))
#met_x = 0; met_y = 0

# WHILE PARA RODAR O JOGO E NAO FECHAR 
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
    if tecla[pygame.K_DOWN] and pos_fogute2_y < 605:
        pos_fogute2_y += 1
    if tecla[pygame.K_LEFT] and pos_fogute2_x > 1:
        pos_fogute2_x -= 1
    if tecla[pygame.K_RIGHT] and pos_fogute2_x < 750:
        pos_fogute2_x += 1
    
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
    if tecla[pygame.K_d] and pos_fogute_y < 740:
        pos_fogute_y += 1
    if tecla[pygame.K_w] and pos_fogute_x > 1:
        pos_fogute_x -= 1
    if tecla[pygame.K_s] and pos_fogute_x < 600:
        pos_fogute_x += 1

    # MOVIMENTOS
    x -= 0.7
    
    # CRIAR IMAGENS DOS DOIS FOGUETES
    screen.blit(foguete, (pos_fogute_y, pos_fogute_x))
    screen.blit(foguete2, (pos_fogute2_x, pos_fogute2_y))
    #screen.blit(meteoro, (met_x, met_y))
    
    pygame.display.update()

pygame.display.quit()

# TO DO 
# 1.0 ARRUMAR O RESPAWN DOS MISSEIS, ELES NAO FUNCIONAM
# 2.0 COLOCAR OS METEOROS ALEATORIOS 
# 3.0 FAZER A COLISAO: 
    # 3.1 FAZER COM QUE SE OS FOGUETES SE COLIDIREM DESCONTA UM PONTO ATE MORREREM
    # 3.2 SE UM DOS MISSESIS ATINGIR O FOGUETE DESCONTA UM PONTO ATE MORREREM 
    # 3.3 SE UM DOS FOGUETES ENCOSTAR NO METEORO DESCONTA UM PONTO ATE MORREREM 