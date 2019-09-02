import json

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

def recupera_nome(json_object, station):
    for dicionario in json_object:
        if station == dicionario['station']:
            return dicionario['name']

def recupera_linha(json_object, station):
    for dicionario in json_object:
        if station == dicionario['station']:
            return dicionario['line']

def get_posicoes():
    pos = {
        'aacd-servidor':(100,20),
        'adolfo-pinheiro':(20,20),
        'alto-da-boa-vista':(20,20),
        'alto-do-ipiranga':(20,20),
        'ana-rosa':(50,40),  #azul
        'anhangabau':(20,20),
        'armenia':(50, 76),  #azul
        'artur-alvim':(20,20),
        'belem':(20,20),
        'borba-gato':(20,20),
        'bras':(20,20),
        'bresser-mooca':(20,20),
        'brigadeiro':(20,20),
        'brooklin':(20,20),
        'butanta':(20,20),
        'camilo-haddad':(20,20),
        'campo-limpo':(20,20),
        'capao-redondo':(20,20),
        'carandiru':(50,84), #azul
        'carrao':(20,20),
        'chacara-klabin':(20,20),
        'clinicas':(20,20),
        'conceicao':(50,16),  #azul
        'consolacao':(20,20),
        'corinthians-itaquera':(20,20),
        'eucaliptos':(20,20),
        'faria-lima':(20,20),
        'fradique-coutinho':(20,20),
        'giovanni-gronchi':(20,20),
        'guilhermina-esperanca':(20,20),
        'higienopolis-mackenzie':(20,20),
        'hospital-sao-paulo':(20,20),
        'jabaquara':(50,12), #azul
        'japao-liberdade':(50, 56), #azul
        'jardim-sao-paulo-ayrton-senna':(50, 92), #azul
        'largo-treze':(20,20),
        'luz':(50,68),  #azul
        'marechal-deodoro':(20,20),
        'moema':(20,20),
        'oratorio':(20,20),
        'oscar-freire':(20,20),
        'palmeiras-barra-funda':(20,20),
        'parada-inglesa':(50, 96), #azul
        'paraiso':(50,44),  #azul
        'patriarca-vila-re':(20,20),
        'paulista':(20,20),
        'pedro-ii':(20,20),
        'penha':(20,20),
        'pinheiros':(20,20),
        'portuguesa-tiete':(50,80),  #azul
        'praca-da-arvore':(50,28),  #azul
        'republica':(20,20),
        'sacoma':(20,20),
        'santa-cecilia':(20,20),
        'santa-cruz':(50,32),  #azul
        'santana':(50,88),  #azul
        'santo-amaro':(20,20),
        'santos-imigrantes':(20,20),
        'santuario-nossa-senhora-de-fatima-sumare':(20,20),
        'sao-bento':(50,64),  #azul
        'sao-joaquim':(50, 52), #azul
        'sao-judas':(50,20),  #azul
        'sao-lucas':(20,20),
        'sao-paulo-morumbi':(20,20),
        'saude':(50,24),  #azul
        'se':(50,60),  #azul
        'tamanduatei':(20,20),
        'tatuape':(20,20),
        'tiradentes':(50,72),  #azul
        'trianon-masp':(20,20),
        'tucuruvi':(50,100), #azul
        'vergueiro':(50,48),  #azul
        'vila-das-belezas':(20,20),
        'vila-madalena':(20,20),
        'vila-mariana':(50,36),  #azul
        'vila-matilde':(20,20),
        'vila-prudente':(20,20),
        'vila-tolstoi':(20,20),
        'vila-uniao':(20,20) }
    return pos


