def BFS(grafo, estacaoOrigem, estacaoDestino):
    explorados = []
    fila = [[estacaoOrigem]]

    if estacaoOrigem == estacaoDestino:
        print('Você já se encontra na estação desejada!')
    
    while fila:
        # print("Explorados")
        # print(explorados)
        caminho = fila.pop(0)
        # print("Caminho")
        # print(caminho)
        no = caminho[-1] # Indice negativo se refere ao ultimo elemento da lista quando não há tamanho fixo
        # print("NO " + no)
        if no not in explorados:
            vizinhos = grafo[no] # Percorre todos os vizinhos daquele no
            # print("Vizinhos")
            # print(vizinhos)
            for vizinho in vizinhos:
                # print("Antes Novo caminho ")
                novo_caminho = list(caminho)
                # print(novo_caminho)
                # print("Depois Novo caminho")
                novo_caminho.append(vizinho)
                # print(novo_caminho)
                # print("Fila")
                fila.append(novo_caminho)
                # print(fila)
                if vizinho == estacaoDestino:
                    return novo_caminho
        explorados.append(no)
    return "Não existe caminho"
    

