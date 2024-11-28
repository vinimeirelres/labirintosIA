import random

"""
Módulo responsável pela implementação do algoritmo de Busca em Profundidade.

Este módulo implementa a busca em profundidade para encontrar um caminho no labirinto, com suporte a:
- Tratamento de células bloqueadas temporariamente.
- Ruído na movimentação (probabilidade de 50% de ordem aleatória).
- Marcação de células visitadas.
- Verificação de célula de destino.[
- Adição de células possíveis na pilha de exploração.
- Retorno de resultados parciais e finais.
"""

def busca_profundidade(labirinto, pilha, objetivo, ruido):
    """
    Executa um passo da busca em profundidade no labirinto.

    Args:
        labirinto (List[List[int]]): Matriz do labirinto atual.
        pilha (List[List[int]]): Pilha de posições a serem exploradas, onde cada posição é [x, y].
        objetivo (List[int]): Coordenadas [x, y] do objetivo.
        ruido (bool): Indica se deve aplicar ruído na ordem de exploração.

    Returns:
        Tuple[bool, Union[List[List[int]], List[int]], List[int]]:
            - bool: True se encontrou o objetivo, False caso contrário.
            - Union[List[List[int]], List[int]]:
                * Se o objetivo **não** foi encontrado: retorna a pilha atualizada (`List[List[int]]`).
                * Se o objetivo foi encontrado: retorna a posição final (`List[int]`).
            - List[int]: Posição atual [x, y].
    """
    posicaoatual = pilha.pop(0)
    x = posicaoatual[0]
    y = posicaoatual[1]
    lab = labirinto[x][y]

    if  posicaoatual == objetivo: # se a posição atual for o destino
        pilha = posicaoatual
        labirinto[x][y] = -1 #marca como visitada
        return True, pilha, posicaoatual
    else: #coloca na fila as posições possíveis

        if labirinto[x][y] == 4:
            pilha.insert(0,[x, y])
            return False, pilha, posicaoatual

        labirinto[x][y] = -1 #marca como visitada

        opcoes = [0, 1, 2, 3]

        #------RUIDO------
        if ruido:
            if random.random() < 0.1:
                random.shuffle(opcoes)
        #---------------------

        for opcao in opcoes:
            if opcao == 0: #Cima
                if (x-1) >=0 and (x-1) < len(labirinto[x]):
                    if labirinto[x-1][y] != 0 and labirinto[x-1][y] != -1:
                        if ([x-1,y] not in pilha):
                            pilha.insert(0,[x-1, y])
            if opcao == 1: #Esquerda
                if (y-1) >=0 and (y-1) < len(labirinto[y]):
                    if labirinto[x][y-1] != 0 and labirinto[x][y-1] != -1:
                        if ([x, y-1] not in pilha):
                            pilha.insert(0,[x, y-1])
            if opcao == 2: #Direita
                if (y+1) >=0 and (y+1) < len(labirinto[y]):
                    if labirinto[x][y+1] != 0  and labirinto[x][y+1] != -1:
                        if ([x, y+1] not in pilha):
                            pilha.insert(0,[x, y+1])
            if opcao == 3: #Baixo
                if (x+1) >=0 and (x+1) < len(labirinto[x]):
                    if labirinto[x+1][y] != 0  and labirinto[x+1][y] != -1:
                        if ([x+1, y] not in pilha):
                            pilha.insert(0,[x+1, y])
        

    return False, pilha, posicaoatual