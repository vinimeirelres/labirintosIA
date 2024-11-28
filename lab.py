from random import random

"""
Módulo responsável pela geração e gerenciamento do labirinto.

Este módulo contém funções para:
- Criar o layout inicial do labirinto
- Gerenciar a matriz de custos para movimentação
- Controlar estados das células do labirinto:
    * 0: caminho livre
    * 1: parede/obstáculo
    * 2: posição inicial
    * 3: objetivo
    * 4: bloqueio temporário
    * -1: célula visitada
-Gerar Bloqueios temporários
-Remover Bloqueios temporários
"""

def getlabirinto():
    """
    Gera uma matriz representando o layout inicial do labirinto.

    Returns:
        List[List[int]]: Matriz onde:
            0: representa caminho livre
            1: representa parede/obstáculo
            2: representa posição inicial (não presente neste layout)
            3: representa objetivo (não presente neste layout)
            4; representa bloqueio temporário (não presente neste layout)
    """
    labirinto = [
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,1,1,1,1,1,1,0],
        [0,1,0,1,0,1,0,0,0,0,1,0],
        [0,0,0,1,0,1,1,1,1,0,1,0],
        [0,1,1,1,1,0,0,0,1,0,1,1],
        [0,0,0,0,1,0,1,0,1,0,1,0],
        [0,1,1,0,1,0,1,0,1,0,1,0],
        [0,0,1,0,1,0,1,0,1,0,1,0],
        [0,1,1,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,1,0,0,0,1,0],
        [1,1,1,1,1,1,1,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    return labirinto

def getcustos(labirinto):
    """
    Gera uma matriz de custos para cada célula do labirinto.

    Args:
        labirinto (List[List[int]]): Matriz do labirinto original

    Returns:
        List[List[float]]: Matriz de custos onde:
            - Células livres (1) ou visitadas (-1) recebem custo (definido ou aleatório)
            - Células com parede (0), bloqueio temporário (4), inicio (2) ou final (3) recebem custo 0
    """
    custos = [linha[:] for linha in labirinto]
    for x, linha in enumerate(labirinto):
        for y, celula in enumerate(linha):
            custo = random()
            #custo = 1
            if celula == 1  or celula == -1:  custos[x][y] = custo
            else: custos[x][y] = 0

    
    return custos

def atualiza_bloqueios(labirinto, probabilidade=0.1):
    """
    Atualiza o estado do labirinto adicionando bloqueios temporários.

    Args:
        labirinto (List[List[int]]): Matriz do labirinto atual
        probabilidade (float, optional): Probabilidade de uma célula ser bloqueada. 
                                       Defaults to 0.1 (10%)

    Returns:
        List[List[int]]: Labirinto atualizado com possíveis novos bloqueios
    """
    novo_labirinto = [linha[:] for linha in labirinto]
    for x in range(len(labirinto)):
        for y in range(len(labirinto[0])):
            if labirinto[x][y] == 1:  # se é um caminho válido
                if random() <  probabilidade:
                    novo_labirinto[x][y] = 4  # bloqueia temporariamente
            elif labirinto[x][y] == -1:  # se é célula visitada
                novo_labirinto[x][y] = -1  # mantém como visitada
    return novo_labirinto

def tira_bloqueios(labirinto):
    """
    Atualiza o estado do labirinto removendo bloqueios temporários.

    Args:
        labirinto (List[List[int]]): Matriz do labirinto atual

    Returns:
        List[List[int]]: Labirinto sem bloqueios temporários
    """
    novo_labirinto = [linha[:] for linha in labirinto]
    for x in range(len(labirinto)):
        for y in range(len(labirinto[0])):
            if labirinto[x][y] == 4:  # se é bloqueio temporário
                novo_labirinto[x][y] = 1  # volta a ser caminho
            elif labirinto[x][y] == -1:  # se é célula visitada
                novo_labirinto[x][y] = -1  # mantém como visitada
    return novo_labirinto