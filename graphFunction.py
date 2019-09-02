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

def menuPrincipal():
    print('Consultrô SP')
    print('Escolha uma das opções abaixo: ')
    print('1 - Encontrar menor caminho entre estações')
    print('0 - Sair')
    opcao = input("O que deseja fazer? ")
    while(opcao != '0' and opcao != '1'):
        print("Opcão inválida! Digite novamente")
        opcao = input("O que deseja fazer? ")
    return opcao

def get_posicoes():
    pos = {
        'aacd-servidor':(30,12), #lilas
        'adolfo-pinheiro':(-22,9), #lilas
        'alto-da-boa-vista':(-12,6), #lilas
        'alto-do-ipiranga':(80,28), #verde
        'ana-rosa':(50,25),  #azul
        'anhangabau':(40,50), #laranja
        'armenia':(50, 70),  #azul
        'artur-alvim':(150,61),#vermelha
        'belem':(85,55), #laranja
        'borba-gato':(0,6), #lilas
        'bras':(67,55), #laranja
        'bresser-mooca':(76,55), #laranja
        'brigadeiro':(38,31),#verde
        'brooklin':(10,6), #lilas
        'butanta':(-38,33),#amarelo
        'camilo-haddad':(135,42), #prata
        'campo-limpo':(-60,22), #lilas
        'capao-redondo':(-70,24), #lilas
        'carandiru':(50,80), #azul
        'carrao':(100,55), #laranja
        'chacara-klabin':(60,23), #lilas,verde
        'clinicas':(4,40), #verde
        'conceicao':(50,-5),  #azul
        'consolacao':(13,35), #verde
        'corinthians-itaquera':(160,64), #laranja
        'eucaliptos':(18, 7), #lilas
        'faria-lima':(-18,33),#amarelo
        'fradique-coutinho':(-5,33), #amarelo
        'giovanni-gronchi':(-40,18), #lilas
        'guilhermina-esperanca':(127,57), #laranja
        'higienopolis-mackenzie':(23,45), #amarelo
        'hospital-sao-paulo':(37,15), #lilas
        'jabaquara':(50,-10), #azul
        'japao-liberdade':(50, 45), #azul
        'jardim-sao-paulo-ayrton-senna':(50, 90), #azul
        'largo-treze':(-28,12), #lilas
        'luz':(50,60),  #azul
        'marechal-deodoro':(5,50), #laranja
        'moema':(23,10), #lilas
        'oratorio':(108,42), #prata
        'oscar-freire':(3,35), #amarelo
        'palmeiras-barra-funda':(-15,50), #laranja
        'parada-inglesa':(50, 95), #azul
        'paraiso':(50,30),  #azul
        'patriarca-vila-re':(140,59), #laranja
        'paulista':(16,40), #amarelo
        'pedro-ii':(60,50), #laranja
        'penha':(106,55), #laranja
        'pinheiros':(-28,33),#amarelo
        'portuguesa-tiete':(50,75),  #azul
        'praca-da-arvore':(50,10),  #azul
        'republica':(30,50), #laranja
        'sacoma':(85,32), #verde
        'santa-cecilia':(20,50), #laranja
        'santa-cruz':(50,15),  #azul
        'santana':(50,85),  #azul
        'santo-amaro':(-34,15), #lilas
        'santos-imigrantes':(75,23), #verde
        'santuario-nossa-senhora-de-fatima-sumare':(-6,40), #verde
        'sao-bento':(50,55),  #azul
        'sao-joaquim':(50, 40), #azul
        'sao-judas':(50,0),  #azul
        'sao-lucas':(120,42), #prata
        'sao-paulo-morumbi':(-50,33), #amarelo
        'saude':(50,5),  #azul
        'se':(50,50),  #azul
        'tamanduatei':(90,37), #verde
        'tatuape':(92,55), #laranja
        'tiradentes':(50,65),  #azul
        'trianon-masp':(27,32),#verde
        'tucuruvi':(50,100), #azul
        'vergueiro':(50,35),  #azul
        'vila-das-belezas':(-47,22), #lilas
        'vila-madalena':(-16,40), #verde
        'vila-mariana':(50,20),  #azul
        'vila-matilde':(115,55), #laranja
        'vila-prudente':(95,42), #verde, prata
        'vila-tolstoi':(160,42), #prata
        'vila-uniao':(150,42) #prata 
        }
    return pos


