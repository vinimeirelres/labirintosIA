import pygame
import sys
from drawing import desenhar_labirinto
import lab
import largura
import profundidade
from time import sleep


pygame.init()

tamanho_celula = 55
largura_janela = 12*tamanho_celula
altura_janela = 12*tamanho_celula
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Projeto 1 - Busca")


labirinto = lab.getlabirinto()
POSICAO_INICIAL = [4,11]
OBJETIVO = [10,0]
algoritmos = {
    'largura': largura.busca_largura,
    'profundidade': profundidade.busca_profundidade
}

def executar_busca(tipo_busca):
    alg = False
    fila = [POSICAO_INICIAL]
    caminho = []

    while not alg:
        alg, fila, posatual = algoritmos[tipo_busca](labirinto, fila, OBJETIVO)  # Busca 
        if posatual:
            caminho.append(posatual)
            sleep(0.5)
            desenhar_labirinto(labirinto,janela,tamanho_celula)  # Desenha o labirinto
            pygame.display.flip()  # Atualiza a tela

        if alg:
            print("Labirinto concluído usando", tipo_busca)
            print(f"Numero de passos: {len(caminho)-1}")
            return caminho
    return None
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                caminho = executar_busca('largura')
            if event.key == pygame.K_p:
                caminho = executar_busca('profundidade')
            if event.key == pygame.K_r:
                labirinto = lab.getlabirinto()
                desenhar_labirinto(labirinto,janela,tamanho_celula)

    janela.fill((255, 255, 255))  # Preenche a janela com branco
    desenhar_labirinto(labirinto,janela,tamanho_celula)  # Desenha o labirinto
    pygame.display.flip()  # Atualiza a tela

