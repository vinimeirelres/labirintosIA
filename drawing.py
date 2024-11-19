import pygame

# Função para desenhar o labirinto
def desenhar_labirinto(labirinto, janela, tamanho_celula, POSICAO_INICIAL, OBJETIVO, EXECUTANDO_BUSCA):
    if not EXECUTANDO_BUSCA:
        labirinto[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = 2
        labirinto[OBJETIVO[0]][OBJETIVO[1]] = 3
    for y, linha in enumerate(labirinto):
        for x, celula in enumerate(linha):
            if celula == 1:  cor = (255, 255, 255)
            elif celula == 2: cor = (255, 0, 0) 
            elif celula == 3:  cor = (0, 255, 0) 
            elif celula == -1: cor = (255, 255, 0)
            else: cor = (0,0,0)
            pygame.draw.rect(janela, cor, (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula))