import pygame
import sys
from drawing import desenhar_labirinto
import lab
import largura
import profundidade
import beamsearch
from time import sleep

"""
Módulo principal que inicializa e coordena a execução dos algoritmos de busca no labirinto.

Este script realiza as seguintes funções:
- Inicializa o Pygame e configura a janela principal.
- Carrega o labirinto a partir do módulo `lab.py`.
- Define a posição inicial e o objetivo no labirinto.
- Controla o loop principal de eventos, incluindo renderização gráfica e interação do usuário.
- Implementa a lógica para alternar entre os diferentes algoritmos de busca:
    * Busca em Largura
    * Busca em Profundidade
    * Beam Search
- Lida com a ativação de funcionalidades opcionais, como ambiente estocástico e ruído na movimentação.
- Exibe informações sobre o caminho encontrado, número de passos e custo total.
"""

pygame.init()

labirinto = lab.getlabirinto()

tamanho_celula = 55
largura_janela = (len(labirinto) * tamanho_celula)+320
altura_janela = (len(labirinto) * tamanho_celula)
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Projeto 1 - Busca")


POSICAO_INICIAL = [4,11]
OBJETIVO = [10,0]
algoritmos = {
    'largura': largura.busca_largura,
    'profundidade': profundidade.busca_profundidade,
    'beam': beamsearch.beam_search
}

ambiente_estocastico = False
ruido = False


def executar_busca(tipo_busca, labirinto):
    """
    Executa o algoritmo de busca especificado no labirinto.

    Args:
        tipo_busca (str): Tipo de algoritmo a ser executado ('largura', 'profundidade' ou 'beam')
        labirinto (List[List[int]]): Matriz do labirinto atual

     Returns:
        Tuple[Optional[List[List[int]]], List[List[int]]]: 
            - Optional[List[List[int]]]: Lista de coordenadas [x,y] do caminho encontrado, ou None se não encontrou
            - List[List[int]]: Matriz do labirinto atualizada após a busca
            
    Utiliza as variáveis globais:
        ambiente_estocastico (bool): Controla bloqueios temporários no labirinto
        ruido (bool): Adiciona aleatoriedade na ordem de expansão dos nós
        POSICAO_INICIAL (List[int]): Coordenadas iniciais
        OBJETIVO (List[int]): Coordenadas do objetivo
    """
    global ambiente_estocastico, ruido #variáveis globais

    alg = False
    fila = [POSICAO_INICIAL]
    beam = []
    caminho = []
    custo = 0
    passos = 0

    while not alg: # Enquanto não encontrar o objetivo
        passos += 1
        
        if (tipo_busca == 'beam'):
            alg, beam, posatual = algoritmos[tipo_busca](labirinto, beam, POSICAO_INICIAL, OBJETIVO, 3)  # Busca
        else:
            alg, fila, posatual = algoritmos[tipo_busca](labirinto, fila, OBJETIVO, ruido)  # Busca 

        custos = lab.getcustos(labirinto)

        #---------AMBIENTE ESTOCÁSTICO----------------
        if ambiente_estocastico:
            if passos % 3 ==  0: #atualiza os bloqueios temporários a cada 5 passos
                labirinto = lab.atualiza_bloqueios(labirinto)
            elif passos % 7 == 0: #tira os bloqueios temporários a cada 7 passos
                labirinto = lab.tira_bloqueios(labirinto)
        #-----------------------------------------------

        if posatual:
            if posatual not in caminho:
                caminho.append(posatual)
            if posatual != POSICAO_INICIAL:
                custo += custos[posatual[0]][posatual[1]]
            sleep(0.5)
            estocastico_button, ruido_button = desenhar_labirinto(labirinto,janela,tamanho_celula, POSICAO_INICIAL, OBJETIVO, 1, ambiente_estocastico, ruido)  # Desenha o labirinto
            pygame.display.flip()  # Atualiza a tela

        if alg:
            print("Labirinto concluído usando", tipo_busca)
            print(f"Caminho: {caminho}")
            print(f"Numero de passos: {len(caminho)-1}")
            print(f"Custo: {custo}")
            return caminho, labirinto
    return None, labirinto
    


while True: #Loop principal
    for event in pygame.event.get(): #Verifica eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: #Verifica teclas pressionadas
            if event.key == pygame.K_l: #Largura
                caminho, labirinto = executar_busca('largura', labirinto)
            if event.key == pygame.K_p: #Profundidade
                caminho, labirinto = executar_busca('profundidade', labirinto)
            if event.key == pygame.K_b: #Beam
                caminho, labirinto = executar_busca('beam', labirinto)
            if event.key == pygame.K_r: #Reiniciar
                labirinto = lab.getlabirinto()
                estocastico_button, ruido_button = desenhar_labirinto(labirinto,janela,tamanho_celula, POSICAO_INICIAL, OBJETIVO, 0, ambiente_estocastico, ruido)
        
        if event.type == pygame.MOUSEBUTTONDOWN: #Verifica cliques do mouse
            mouse_pos = event.pos
            if estocastico_button.collidepoint(mouse_pos):
                ambiente_estocastico = not ambiente_estocastico
            if ruido_button.collidepoint(mouse_pos):
                ruido = not ruido

    janela.fill((255, 255, 255))  # Preenche a janela com branco
    estocastico_button, ruido_button = desenhar_labirinto(labirinto,janela,tamanho_celula, POSICAO_INICIAL, OBJETIVO, 0, ambiente_estocastico, ruido)  # Desenha o labirinto
    pygame.display.flip()  # Atualiza a tela

