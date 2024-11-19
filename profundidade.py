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
        labirinto[x][y] = -1 #marca como visitada

        #Cima
        if labirinto[x-1][y] != 0 and labirinto[x-1][y] != -1:
            if ([x-1,y] not in pilha):
                pilha.insert(0,[x-1, y])
        #Esquerda
        if labirinto[x][y-1] != 0 and labirinto[x][y-1] != -1:
            if ([x, y-1] not in pilha):
                pilha.insert(0,[x, y-1])
        #Direita
        if labirinto[x][y+1] != 0  and labirinto[x][y+1] != -1:
            if ([x, y+1] not in pilha):
                pilha.insert(0,[x, y+1])
       #Baixo
        if labirinto[x+1][y] != 0  and labirinto[x+1][y] != -1:
            if ([x+1, y] not in pilha):
                pilha.insert(0,[x+1, y])
        

    return False, pilha, posicaoatual