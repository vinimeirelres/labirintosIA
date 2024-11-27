from random import random

def getlabirinto():
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
    custos = [linha[:] for linha in labirinto]
    for x, linha in enumerate(labirinto):
        for y, celula in enumerate(linha):
            custo = random()
            #custo = 1
            if celula == 1  or celula == -1:  custos[x][y] = custo
            else: custos[x][y] = 0

    
    return custos

def atualiza_bloqueios(labirinto, probabilidade=0.1):
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
    novo_labirinto = [linha[:] for linha in labirinto]
    for x in range(len(labirinto)):
        for y in range(len(labirinto[0])):
            if labirinto[x][y] == 4:  # se é bloqueio temporário
                novo_labirinto[x][y] = 1  # volta a ser caminho
            elif labirinto[x][y] == -1:  # se é célula visitada
                novo_labirinto[x][y] = -1  # mantém como visitada
    return novo_labirinto