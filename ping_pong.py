#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import random
import sys
import time

def game(player_name,player2_name):
    pygame.init()

    '''
    Região do Programa que Define as Variáveis
    '''

    #Variáveis que Define proporções da Tela
    largura_x = 800
    altura_y = 600

    #Definindo Tela do Game
    janela = pygame.display.set_mode((largura_x, altura_y))
    pygame.display.set_caption("Ping Pong")

    #Definindo FPS (Frames por Segundo)
    fps = pygame.time.Clock()

    #Definindo variáveis de inicialização de mensagens
    fonte = pygame.font.SysFont('arial', 25, bold=True, italic=True)
    fonte2 = pygame.font.SysFont('arial', 30, bold=True, italic=True)
    msg1 = True
    msg_player = False
    msg_oponente = False 
    player1_vitoria = False
    player2_vitoria = False
    temporizador = False
    pontos_player1 = 0
    pontos_player2 = 0
    temporizador_inicial = 3

    #Definindo variáveis de inicialização do programa
    iniciar_game = False
    arremesso_inicial = random.randint(1, 2)

    #Definindo variáveis de Objetos do Game
    raquete_x = 760
    raquete_y = 215
    oponente_x = 18
    oponente_y = 215
    bola_x = 385
    bola_y = 260
    velocidade_bola_x = random.uniform(2.0, 2.9)
    velocidade_bola_y = random.uniform(2.0, 2.9)
    parede1_x = 1
    parede1_y = 43
    parede2_x = 1
    parede2_y = 557

    while (True):
        fps.tick(300) #Definição do FPS do Game
        janela.fill((0,0,0)) #Preencher a Tela a cada Update
    
        '''
        Região de Mensagens do Game
        '''
        mensagem_inicial = "Pressione E para iniciar o Game!"
        mensagem_player = "{0}" .format(player_name)
        mensagem_oponente = "{0}" .format(player2_name)
        mensagem_vitoria_p1 = "O {0} venceu o Game!" .format(player_name)
        mensagem_vitoria_p2 = "O {0} venceu o Game!" .format(player2_name)
        placar = "{0}x{1}" .format(pontos_player1,pontos_player2)
        tempo_inicial = "{0}" .format(temporizador_inicial)
        restart_msg = "Pressione R para Reiniciar o Game"

        texto_formatado = fonte2.render(mensagem_inicial, True, (255,255,255))
        texto_formatado2 = fonte.render(mensagem_player, True, (255,255,255))
        texto_formatado3 = fonte.render(mensagem_oponente, True, (255,255,255))
        texto_formatado4 = fonte.render(mensagem_vitoria_p1, True, (255,255,255))
        texto_formatado5 = fonte.render(mensagem_vitoria_p2, True, (255,255,255))
        texto_formatado6 = fonte.render(placar, True, (255,255,255))
        texto_formatado7 = fonte.render(tempo_inicial, True, (255,255,51))
        texto_formatado8 = fonte.render(restart_msg, True, (255,255,51))

        '''
        Laço de repetição que atualiza o Game constantemente
        '''
        for event in pygame.event.get():
            '''
            Desvios condicionais que definem eventos de teclas e movimentos únicos
            '''
            if (event.type == QUIT):
                pygame.quit()
                sys.exit(1)

            if (event.type == KEYDOWN):
                if (event.key == K_e):
                    msg1 = False
                    iniciar_game = True

            if (event.type == KEYDOWN):
                if (event.key == K_r):
                    game(player_name,player2_name) 

        if (pygame.key.get_pressed()[K_w]):
            oponente_y -= 2
        
        if (pygame.key.get_pressed()[K_s]):
            oponente_y += 2

        if (pygame.key.get_pressed()[K_UP]):
            raquete_y -= 2
        
        if (pygame.key.get_pressed()[K_DOWN]):
            raquete_y += 2

        if (msg1 == True):
            janela.blit(texto_formatado, (150,280))
        
        if (msg_player == True):
            janela.blit(texto_formatado2, (690,10))
            janela.blit(texto_formatado3, (18,10))

        if (iniciar_game == True):
            msg_player = True 
            msg_oponente = True

            player1 = pygame.draw.rect(janela, (74,117,173), (raquete_x,raquete_y,20,150))
            player2 = pygame.draw.rect(janela, (207,21,186), (oponente_x,oponente_y,20,150))
            bola = pygame.draw.rect(janela, (255,255,255), (bola_x,bola_y,20,20))
            pygame.draw.rect(janela, (118,205,210), (parede1_x,parede1_y,800,10))
            pygame.draw.rect(janela, (118,205,210), (parede2_x,parede2_y,800,10))
            
            iniciar_game = True

            #Se a bola colidir com a Raquete do Jogador
            if (player2.colliderect(bola)):
                if (bola_x <= oponente_x):
                    variacao = random.randint(1, 2)
                    if (variacao == 1):
                        #Transforme os valores positivos e negativos
                        velocidade_bola_y = +velocidade_bola_x
                        velocidade_bola_x = -velocidade_bola_y

                    else:
                        velocidade_bola_y = -velocidade_bola_x
                        velocidade_bola_x = +velocidade_bola_y

            #Se a bola colidir com a Raquete do Jogador
            if (player1.colliderect(bola)):
                if (bola_x >= raquete_x):
                    variacao = random.randint(1, 2)
                    if (variacao == 1):
                        #Transforme os valores positivos e negativos
                        velocidade_bola_y = +velocidade_bola_x
                        velocidade_bola_x = -velocidade_bola_y

                    else:
                        velocidade_bola_y = -velocidade_bola_x
                        velocidade_bola_x = +velocidade_bola_y

        if (iniciar_game == True):
            temporizador = True
            janela.blit(texto_formatado6, (385,10))
            if (arremesso_inicial == 1):
                bola_x -= velocidade_bola_x
                bola_y += velocidade_bola_y
   
            elif (arremesso_inicial == 2):
                bola_x += velocidade_bola_x
                bola_y -= velocidade_bola_y

        if (temporizador == True):
            if (temporizador_inicial <= -1):
                temporizador = False
            
            else:
                time.sleep(1.5)
                temporizador_inicial -= 1
                janela.blit(texto_formatado7, (385,300))

        if (raquete_y <= 55):
            raquete_y = 55

        if (raquete_y >= 405):
            raquete_y = 405

        if (oponente_y <= 55):
            oponente_y = 55

        if (oponente_y >= 405):
            oponente_y = 405

        if (bola_y >= parede2_y):
            velocidade_bola_y = -velocidade_bola_y

        if (bola_y <= parede1_y):
            velocidade_bola_y = -velocidade_bola_y

        if (bola_x < 1):
            if (pontos_player2 >= 4):
                pontos_player2 += 1
                player2_vitoria = True
                velocidade_bola_x = 0
                velocidade_bola_y = 0 
                bola_x = 385
                bola_y = 260

            else:
                bola_x = 385
                bola_y = 260
                pontos_player2 += 1

        if (bola_x > 800):
            if (pontos_player1 >= 4):
                pontos_player1 += 1
                player1_vitoria = True
                velocidade_bola_x = 0
                velocidade_bola_y = 0 
                bola_x = 385
                bola_y = 260

            else:
                bola_x = 385
                bola_y = 260
                pontos_player1 += 1

        if (player2_vitoria == True):
            janela.blit(texto_formatado4, (250,280))
            janela.blit(texto_formatado8, (250,350))

        if (player1_vitoria == True):
            janela.blit(texto_formatado5, (250,280))
            janela.blit(texto_formatado8, (250,350))

        pygame.display.flip()

player_name = str(input("Digite o Nome do Jogador 1: "))
player2_name = str(input("Digite o Nome do Jogador 2: "))

game(player_name,player2_name)
