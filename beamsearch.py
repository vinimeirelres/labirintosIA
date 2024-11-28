"""
Módulo responsável pela implementação do algoritmo Beam Search (Busca em Feixe).

Este módulo implementa a busca heurística Beam Search para encontrar um caminho no labirinto,
com suporte a:
- Tratamento de células bloqueadas temporariamente.
- Marcação de células visitadas.
- Limitação do feixe para otimizar a busca.
"""

def heuristica(a, b): # Distância de Manhattan
        """
    Calcula a distância de Manhattan entre duas posições.

    Args:
        a (List[int]): Coordenadas [x, y] da primeira posição.
        b (List[int]): Coordenadas [x, y] da segunda posição.

    Returns:
        int: Distância de Manhattan entre as posições `a` e `b`.
    """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

def beam_search(labirinto, beam, inicial, objetivo, beam_width):
    """
    Executa um passo da busca Beam Search no labirinto.

    Args:
        labirinto (List[List[int]]): Matriz do labirinto atual.
        fila (List[Dict]): Lista de nós a serem explorados, onde cada nó é um dicionário contendo:
            - 'posicao': List[List[int]] -> Coordenadas [x, y] de todas as posições percorridas, a posição atual será a última da lista.
            - 'h_score': float -> Valor heurístico associado ao nó.
        objetivo (List[int]): Coordenadas [x, y] do objetivo.
        beam_width (int): Número máximo de nós mantidos em cada nível (largura do feixe).

    Returns:
        Tuple[bool, Union[List[Dict], List[List[int]]]]:
            - bool: True se encontrou o objetivo, False caso contrário.
            - Union[List[Dict], List[List[int]]]:
                * Se o objetivo **não** foi encontrado: retorna a fila atualizada (`List[Dict]`).
                * Se o objetivo foi encontrado: retorna o caminho encontrado (`List[List[int]]`).
    """
    
    if not beam:
        beam = [{'posicao': [inicial], 
                'h_score': heuristica(inicial, objetivo)}]
    
    if len(beam) == 0: # Se não houver caminho, não há como continuar
        return False, [], None
        
    beam = sorted(beam, key=lambda x: x['h_score'])[:beam_width] #organiza o beam pelo h_score e pega os primeiros beam_width

    atual = beam.pop(0)
    posicaoatual = atual['posicao'][-1]
    x, y = posicaoatual
    
    if posicaoatual == objetivo:
        return True, atual['posicao'], posicaoatual
    else: #adiciona as posições possíveis no beam
        novo_beam = beam.copy()
        
        if labirinto[x][y] == 4:
            novo_beam.append({
                'posicao': atual['posicao'],
                'h_score': atual['h_score']
            })       
            if len(beam) > 0:
                atual = beam.pop(0)
                posicaoatual = atual['posicao'][-1]
                x, y = posicaoatual
            else:
                return False, novo_beam, posicaoatual

        labirinto[x][y] = -1

        #introduzir incerteza no beam search não faz sentido, pois o algoritmo reorganiza o beam segundo a heurística para escolher o próximo passo

        #Cima
        if (x-1) >= 0 and (x-1) < len(labirinto):
            if labirinto[x-1][y] != 0 and labirinto[x-1][y] != -1:
                if [x-1,y] not in novo_beam:
                    novo_caminho = atual['posicao'] + [[x-1, y]]
                    h_score = heuristica([x-1, y], objetivo)
                    novo_beam.append({
                        'posicao': novo_caminho,
                        'h_score': h_score
                    })

        #Esquerda
        if (y-1) >= 0 and (y-1) < len(labirinto[0]):
            if labirinto[x][y-1] != 0 and labirinto[x][y-1] != -1:
                if [x,y-1] not in novo_beam:
                    novo_caminho = atual['posicao'] + [[x, y-1]]
                    h_score = heuristica([x, y-1], objetivo)
                    novo_beam.append({
                        'posicao': novo_caminho,
                        'h_score': h_score
                    })

        #Direita
        if (y+1) >= 0 and (y+1) < len(labirinto[0]):
            if labirinto[x][y+1] != 0 and labirinto[x][y+1] != -1:
                if [x,y+1] not in novo_beam:
                    novo_caminho = atual['posicao'] + [[x, y+1]]
                    h_score = heuristica([x, y+1], objetivo)
                    novo_beam.append({
                        'posicao': novo_caminho,
                        'h_score': h_score
                    })

        #Baixo
        if (x+1) >= 0 and (x+1) < len(labirinto):
            if labirinto[x+1][y] != 0 and labirinto[x+1][y] != -1:
                if [x+1,y] not in novo_beam:
                    novo_caminho = atual['posicao'] + [[x+1, y]]
                    h_score = heuristica([x+1, y], objetivo)
                    novo_beam.append({
                        'posicao': novo_caminho,
                        'h_score': h_score
                    })

    return False, novo_beam, posicaoatual