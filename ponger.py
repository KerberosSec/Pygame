#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
import random

def game():
   pygame.init()

   largura_x = 800
   altura_y = 600

   janela = pygame.display.set_mode((largura_x, altura_y))
   pygame.display.set_caption("Ponger")

   raquete_x = 340
   raquete_y = 550

   bola_x = random.randint(1, 705)
   bola_y = 1

   queda = False
   velocidade = 0.85

   fps = pygame.time.Clock()

   vida = 5
   score = 0

   fonte = pygame.font.SysFont('arial', 30, bold=True, italic=True)
   msg = True
   msg2 = False

   while (True):
      fps.tick(300)
      janela.fill((0,0,0))

      mensagem_inicial = "Pressione E para comecar o Game!"
      mensagem = "Vida: {0}" .format(vida)
      mensagem2 = "Score: {0}" .format(score)
      mensagem3 = "Voce Perdeu o Game!"
      mensagem4 = "Seu Score foi de {0} pontos" .format(score)
      mensagem5 = "Pressione R para Reiniciar o Game!"

      texto_formatado = fonte.render(mensagem, True, (255,255,255))
      texto_formatado2 = fonte.render(mensagem2, True, (255,255,255))
      texto_formatado3 = fonte.render(mensagem_inicial, True, (255,255,255))
      texto_formatado4 = fonte.render(mensagem3, True, (255,255,255))
      texto_formatado5 = fonte.render(mensagem4, True, (255,0,255))
      texto_formatado6 = fonte.render(mensagem5, True, (255,255,255))

      for event in pygame.event.get():
         if (event.type == QUIT):
             pygame.quit()
             sys.exit(1)

         if (event.type == KEYDOWN):
            if (event.key == K_e):
                queda = True
                msg = False
                msg2 = True

         if (event.type == KEYDOWN):
            if (event.key == K_r):
                game()

      raquete = pygame.draw.rect(janela, (0,255,255), (raquete_x,raquete_y,100,20))
      bola = pygame.draw.rect(janela, (0,255,0), (bola_x,bola_y,30,30))

      if pygame.key.get_pressed()[K_a]:
          raquete_x -= 3
          if (raquete_x <= 1):
              raquete_x = 1

      if pygame.key.get_pressed()[K_d]:
          raquete_x += 3
          if (raquete_x >= 700):
              raquete_x = 700

      if (queda == True):
          if (velocidade >= 3):
              bola_y += 3

          else:
              bola_y += velocidade

      if (raquete.colliderect(bola)):
          bola_x = random.randint(1, 705)
          bola_y = 1
          velocidade += 0.25
          score += 1

      if (bola_y > 552):
          if (vida <= 1):
              msg2 = False
              janela.blit(texto_formatado4, (180,250))
              janela.blit(texto_formatado5, (180,300))
              janela.blit(texto_formatado6, (130,400))

          else:
              vida -= 1
              bola_x = random.randint(1, 705)
              bola_y = 1

      if (msg == True):
          janela.blit(texto_formatado3, (150,280))

      if (msg2 == True):
          janela.blit(texto_formatado, (100,40))
          janela.blit(texto_formatado2, (100,80))

      pygame.display.flip()

game()
