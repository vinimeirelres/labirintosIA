import pygame
import sys
from drawing import desenhar_labirinto
import lab
import largura
import profundidade
import beamsearch
from time import sleep


pygame.init()

labirinto = lab.getlabirinto()

tamanho_celula = 55
largura_janela = (len(labirinto) * tamanho_celula)+210
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
    global ambiente_estocastico, ruido

    alg = False
    fila = [POSICAO_INICIAL]
    beam = []
    caminho = []
    custo = 0
    passos = 0

    while not alg:
        passos += 1
        
        if (tipo_busca == 'beam'):
            alg, beam, posatual = algoritmos[tipo_busca](labirinto, beam, POSICAO_INICIAL, OBJETIVO, 3)  # Busca
        else:
            alg, fila, posatual = algoritmos[tipo_busca](labirinto, fila, OBJETIVO, ruido)  # Busca 

        #---------AMBIENTE ESTOCÁSTICO----------------
        if ambiente_estocastico:
            if passos % 3 ==  0: #atualiza os bloqueios temporários a cada 5 passos
                labirinto = lab.atualiza_bloqueios(labirinto)
            elif passos % 7 == 0: #tira os bloqueios temporários a cada 7 passos
                labirinto = lab.tira_bloqueios(labirinto)
        #-----------------------------------------------

        custos = lab.getcustos(labirinto)

        if posatual:
            if posatual not in caminho:
                caminho.append(posatual)
            print(custos[posatual[0]][posatual[1]])
            custo += custos[posatual[0]][posatual[1]]
            #print(custo)
            sleep(0.5)
            estocastico_button, ruido_button = desenhar_labirinto(labirinto,janela,tamanho_celula, POSICAO_INICIAL, OBJETIVO, 1, ambiente_estocastico, ruido)  # Desenha o labirinto
            pygame.display.flip()  # Atualiza a tela

        if alg:
            custo += custos[posatual[0]][posatual[1]]
            print("Labirinto concluído usando", tipo_busca)
            print(f"Caminho: {caminho}")
            print(f"Numero de passos: {len(caminho)-1}")
            print(f"Custo: {custo}")
            return caminho, labirinto
    return None, labirinto
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                caminho, labirinto = executar_busca('largura', labirinto)
            if event.key == pygame.K_p:
                caminho, labirinto = executar_busca('profundidade', labirinto)
            if event.key == pygame.K_b:
                caminho, labirinto = executar_busca('beam', labirinto)
            if event.key == pygame.K_r:
                labirinto = lab.getlabirinto()
                estocastico_button, ruido_button = desenhar_labirinto(labirinto,janela,tamanho_celula, POSICAO_INICIAL, OBJETIVO, 0, ambiente_estocastico, ruido)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if estocastico_button.collidepoint(mouse_pos):
                ambiente_estocastico = not ambiente_estocastico
            if ruido_button.collidepoint(mouse_pos):
                ruido = not ruido

    janela.fill((255, 255, 255))  # Preenche a janela com branco
    estocastico_button, ruido_button = desenhar_labirinto(labirinto,janela,tamanho_celula, POSICAO_INICIAL, OBJETIVO, 0, ambiente_estocastico, ruido)  # Desenha o labirinto
    pygame.display.flip()  # Atualiza a tela

