import pygame

# Função para desenhar o labirinto
def desenhar_labirinto(labirinto, janela, tamanho_celula, POSICAO_INICIAL, OBJETIVO, EXECUTANDO_BUSCA):
    if EXECUTANDO_BUSCA == 0:
        labirinto[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = 2
        labirinto[OBJETIVO[0]][OBJETIVO[1]] = 3
    for y, linha in enumerate(labirinto):
        for x, celula in enumerate(linha):
            celula = int(celula)
            if celula == 1:  cor = (255, 255, 255)
            elif celula == 2: cor = (255,182,193) 
            elif celula == 3:  cor = (144,238,144) 
            elif celula == -1: cor = (255, 255, 153)
            elif celula == 4: cor = (204,229,255) #para bloqueios temporários
            else: cor = (211,211,211)
            pygame.draw.rect(janela, cor, (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula))
            pygame.draw.rect(janela, (0, 0, 0), (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula), 1)  # Borda preta