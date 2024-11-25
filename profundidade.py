import random

def busca_profundidade(labirinto, pilha, objetivo):
    posicaoatual = pilha.pop(0)
    x = posicaoatual[0]
    y = posicaoatual[1]
    lab = labirinto[x][y]

    if  posicaoatual == objetivo: # se a posição atual for o destino
        pilha = labirinto[x][y]
        labirinto[x][y] = -1 #marca como visitada
        return True, pilha, posicaoatual
    else: #coloca na fila as posições possíveis

        if labirinto[x][y] == 4:
            pilha.append([x, y])
            return False, pilha, posicaoatual

        labirinto[x][y] = -1 #marca como visitada

        opcoes = [0, 1, 2, 3]

        #------RUIDO------
        #if random.random() < 0.1:
            #random.shuffle(opcoes)
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