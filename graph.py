import pandas as pd
import json
import matplotlib.pyplot as plt
from networkx import nx
from graphFunction import *

def main():
    df = pd.read_csv('metrosp_stations.csv')
    df =  df.drop(columns=['Unnamed: 0'])
    df.neigh = df.neigh.str[1:-1].str.split(',').tolist()
    df = df.neigh.apply(pd.Series) \
    .merge(df, left_index = True, right_index = True) \
    .drop(["neigh"], axis = 1) \
    .melt(id_vars = ['name','station','lat', 'lon', 'line'], value_name = "onlyNeigh") \
    .drop("variable", axis = 1) \
    .dropna()
    df.to_json('metroSP.json')

    with open('metroSPNotEdited.json') as json_file:
        dataNotEdited = json.load(json_file)

    with open('metroSP.json') as json_file:
        data = json.load(json_file)

    listaDeAdjacencia = {}
    listaEstacoes = []

    # Montando lista de adjacência
    for (key, estacao) in data['station'].items():
        if not listaDeAdjacencia.get(estacao):
            listaDeAdjacencia[estacao] = []
            listaEstacoes.append(estacao)

        listaDeAdjacencia[estacao].append(data['onlyNeigh'][key])

    # Salvando lista de adjacência
    with open('listaAdjacencia.json', 'w') as json_file:
        json.dump(listaDeAdjacencia, json_file)
    
    # print(listaDeAdjacencia)
    print(BFS(listaDeAdjacencia, 'campo-limpo', 'largo-treze'))

    # print(dataNotEdited['name'].get('0'))

    G = nx.Graph()
    labels = {}
    mapaDeCores = []

    for estacao, arestas in listaDeAdjacencia.items():  

        corNo = recupera_linha(dataNotEdited, estacao)
        labels[estacao] = recupera_nome(dataNotEdited, estacao)  
        G.add_node(estacao)  
        # corNo = nx.get_node_attributes(G,'color')
        # corNo = recupera_linha(dataNotEdited, estacao)
        if corNo == '[lilas]':
            mapaDeCores.append('#8B008B')
        elif corNo == '[verde]':
            mapaDeCores.append('#006400')
        elif corNo == '[azul]':
            
            mapaDeCores.append('#000080')
        elif corNo == '[vermelha]':
            mapaDeCores.append('#FF0000')
        elif corNo == '[amarela]':
            mapaDeCores.append('#FFFF00')
        elif corNo == '[prata]':
            mapaDeCores.append('#C0C0C0')
        else:
            mapaDeCores.append('#FFDAB9')

        for aresta in arestas:
            G.add_edge(estacao, aresta)

    print(mapaDeCores)
    
    listaNos = G.nodes()
    listaNos = sorted((set(listaNos)))
    posicoes = get_posicoes()

    nx.draw(G, pos=posicoes, nodelist=listaNos,with_labels=True,labels=labels, node_color=mapaDeCores)
    plt.show()

main()
