import pygame
"""
Módulo responsável pela interface gráfica do labirinto usando Pygame.

Este módulo contém funções para renderizar o labirinto, botões de controle
e elementos visuais da simulação.
"""

# Função para desenhar o labirinto
def desenhar_labirinto(labirinto, janela, tamanho_celula, POSICAO_INICIAL, OBJETIVO, EXECUTANDO_BUSCA, ambiente_estocastico, ruido):
    """
    Desenha o labirinto e elementos da interface na janela do Pygame.

    Args:
        labirinto (List[List[int]]): Matriz do labirinto (lista 2D)
        janela (pygame.Surface): Superfície de desenho do Pygame
        tamanho_celula (int): Dimensão em pixels de cada célula
        POSICAO_INICIAL (List[int]): Lista [x,y] da posição inicial
        OBJETIVO (List[int]): Lista [x,y] do objetivo
        EXECUTANDO_BUSCA (bool): Estado atual da busca
        ambiente_estocastico (bool): Estado do modo estocástico
        ruido (bool): Estado do modo com ruído


    Returns:
        Bool: Estado do botão de ambiente estocástico
        Bool: Estado do botão de ruído
    
    Detalhes:
        - Desenha o labirinto na janela do Pygame
        - Desenha as posições inicial e final do labirinto
        - Desenha as células bloqueadas temporariamente
        - Desenha o caminho percorrido durante a busca
        - Desenha botões para controle do ambiente estocástico e ruído
        - Utiliza cores diferentes para indicar estados dos botões:
            * Ambiente estocástico: Azul claro quando ativo, Rosa claro quando inativo
            * Ruído: Verde claro quando ativo, Bege claro quando inativo
        - Renderiza textos usando fonte Consolas tamanho 24
    """
    font = pygame.font.SysFont('Consolas', 24)
    altura_janela = janela.get_height()
    largura_janela = janela.get_width()

    # Botão do Ambiente estocástico
    estocastico_button = pygame.Rect(largura_janela - 310, 50, 280,30)
    estocastico_color = (176, 196, 222) if ambiente_estocastico else (255, 182, 193)  
    pygame.draw.rect(janela, estocastico_color, estocastico_button)
    se_text = font.render('Ambiente Estocástico', True, (0, 0, 0))
    janela.blit(se_text, (estocastico_button.x + 5, estocastico_button.y + 5))

    # Botao Ruido
    ruido_button = pygame.Rect(largura_janela - 310, 100, 160, 30)
    ruido_color = (152, 251, 152) if ruido else (255, 228, 196)  # Tons pastéis
    pygame.draw.rect(janela, ruido_color, ruido_button)
    noise_text = font.render('Ruído', True, (0, 0, 0))
    janela.blit(noise_text, (ruido_button.x + 5, ruido_button.y + 5))

    
    if EXECUTANDO_BUSCA == 0:
        labirinto[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = 2
        labirinto[OBJETIVO[0]][OBJETIVO[1]] = 3
    for x, linha in enumerate(labirinto):
        for y, celula in enumerate(linha):
            celula = int(celula)
            if celula == 1:  cor = (255, 255, 255)
            elif celula == 2: cor = (255,182,193) 
            elif celula == 3:  cor = (144,238,144) 
            elif celula == -1: cor = (255, 255, 153)
            elif celula == 4: cor = (204,229,255) #para bloqueios temporários
            else: cor = (211,211,211)
            pygame.draw.rect(janela, cor, (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula))
            pygame.draw.rect(janela, (0, 0, 0), (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula), 1)  # Borda preta

            #Colocar A e B na poisção inicial e final ]
            centro = (y * tamanho_celula + tamanho_celula // 2, x * tamanho_celula + tamanho_celula // 2)
            if (x,y) == tuple(POSICAO_INICIAL):   
                texto_inicial = font.render('A', True, (0, 0, 0))
                texto_inicial_rect = texto_inicial.get_rect(center=centro)
                janela.blit(texto_inicial, texto_inicial_rect)
            elif (x,y) == tuple(OBJETIVO):
                texto_final = font.render('B', True, (0, 0, 0))
                texto_final_rect = texto_final.get_rect(center=centro)
                janela.blit(texto_final, texto_final_rect)
    
    return estocastico_button, ruido_button