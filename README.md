# Labirintos IA

Este projeto demonstra algoritmos de busca clássicos aplicados a um labirinto 2D usando **Pygame** para exibir o processo passo a passo. O código foi desenvolvido como parte de um trabalho da disciplina de SIN323 - Inteligência Artificial da Universidade Federal de Viçosa - Campus Rio Paranaíba.

## Algoritmos implementados

- **Busca em Largura (BFS)** – implementação no arquivo `largura.py`.
- **Busca em Profundidade (DFS)** – implementação no arquivo `profundidade.py`.
- **Beam Search** – implementação no arquivo `beamsearch.py`.

O arquivo `main.py` orquestra a aplicação: inicializa o Pygame, carrega o labirinto e permite alternar entre os algoritmos.

## Requisitos

- Python 3.11 ou superior
- [Pygame](https://www.pygame.org/) (`pip install pygame`)

## Executando

1. Instale as dependências:
   ```bash
   pip install pygame
   ```
2. Execute o script principal:
   ```bash
   python main.py
   ```

Uma janela será aberta mostrando o labirinto. Use as seguintes teclas para iniciar cada busca:

- **L** – Busca em Largura
- **P** – Busca em Profundidade
- **B** – Beam Search
- **R** – Reinicia o labirinto

Durante a execução, clique nos botões da interface para ativar o **Ambiente Estocástico** (adiciona/remove bloqueios temporários) e o **Ruído** (aleatoriza a ordem de expansão)【F:main.py†L120-L139】.

A posição inicial (`POSICAO_INICIAL`) e o objetivo (`OBJETIVO`) são definidos em `main.py`, e o layout do labirinto está em `lab.py`.

## Estrutura do projeto

```
beamsearch.py      # Algoritmo Beam Search
largura.py         # Busca em Largura
profundidade.py    # Busca em Profundidade
drawing.py         # Funções de renderização com Pygame
lab.py             # Definição do labirinto e custos
main.py            # Loop principal da aplicação
```

## Personalização

- Para alterar o labirinto ou a probabilidade de bloqueios temporários, edite as funções em `lab.py`.
- Para modificar a largura do feixe na Beam Search, ajuste o argumento `beam_width` em `main.py` na chamada do algoritmo.

---

Este projeto exemplifica técnicas de busca em IA com visualização interativa e pode servir de base para experimentos ou estudos sobre algoritmos de navegação em labirintos.
