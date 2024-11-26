import pygame

# Função para desenhar o labirinto
def desenhar_labirinto(labirinto, janela, tamanho_celula, POSICAO_INICIAL, OBJETIVO, EXECUTANDO_BUSCA, ambiente_estocastico, ruido):
    font = pygame.font.SysFont(None, 24)
    altura_janela = janela.get_height()
    largura_janela = janela.get_width()

    # Botão do Ambiente estocástico
    estocastico_button = pygame.Rect(largura_janela - 190, 50, 180,30)
    estocastico_color = (0, 255, 0) if ambiente_estocastico else (255, 0, 0)
    pygame.draw.rect(janela, estocastico_color, estocastico_button)
    se_text = font.render('Ambiente Estocástico', True, (255, 255, 255))
    janela.blit(se_text, (estocastico_button.x + 5, estocastico_button.y + 5))

    # Botao Ruido
    ruido_button = pygame.Rect(largura_janela - 180, 100, 160, 30)
    ruido_color = (0, 255, 0) if ruido else (255, 0, 0)
    pygame.draw.rect(janela, ruido_color, ruido_button)
    noise_text = font.render('Ruído', True, (255, 255, 255))
    janela.blit(noise_text, (ruido_button.x + 5, ruido_button.y + 5))

    
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
    
    return estocastico_button, ruido_button