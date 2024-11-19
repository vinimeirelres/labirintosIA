import pygame
import sys
from drawing import desenhar_labirinto
import lab
import largura
import profundidade
from time import sleep


pygame.init()

largura_janela = 600
altura_janela = 600
tamanho_celula = 50

# Cria a janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Labirinto")

labirinto = lab.getlabirinto()
alg = False
caminho = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    janela.fill((255, 255, 255))  # Preenche a janela com branco
    fila = [[10,0]]
    while not alg:
        #print(fila)
        alg, fila, posatual = profundidade.busca_profundidade(labirinto, fila)  # Busca em largura
        caminho.append(posatual)
        sleep(0.5)
        desenhar_labirinto(labirinto,janela,tamanho_celula)  # Desenha o labirinto
        pygame.display.flip()  # Atualiza a tela
        if alg:
            print(len(caminho))
    desenhar_labirinto(labirinto,janela,tamanho_celula)  # Desenha o labirinto
    pygame.display.flip()  # Atualiza a tela

