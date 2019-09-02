import pandas as pd
import json
import matplotlib.pyplot as plt
import os
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
    
    
    while True:
        os.system("clear")
        opcao = menuPrincipal()
        if opcao == '1':
            origem = input("Estação de Origem: ")
            destino = input("Estação de Destino: ")
            menor_caminho = BFS(listaDeAdjacencia, origem, destino)
            print('Esse é o menor caminho para chegar no seu destino:')
            for item in menor_caminho:
                print(recupera_nome(dataNotEdited, item)+' - ' +recupera_linha(dataNotEdited, item))
            
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
                    mapaDeCores.append('#FF8C00')
                elif corNo == '[prata]':
                    mapaDeCores.append('#1C1C1C')
                else:
                    mapaDeCores.append('#8B4513')

                for aresta in arestas:
                    G.add_edge(estacao, aresta)

            listaNos = G.nodes()
            listaNos = sorted((set(listaNos)))
            posicoes = get_posicoes()

            fig1 = plt.figure('Grafo Principal')
            nx.draw(G, pos=posicoes, nodelist=listaNos,with_labels=True,labels=labels, node_color=mapaDeCores, font_size = 6, font_color = 'white', edge_color = '#A0522D')
            fig1.set_facecolor("#00000F")


            fig2 = plt.figure('Subgrafo')
            fig2.set_facecolor("#00000F")
            ax = plt.gca()
            ax.set_facecolor('#00000F')
            subgraph = G.subgraph(menor_caminho)                
            nx.draw_networkx(subgraph, pos=posicoes, font_size = 8,edge_color = '#00CED1', node_color = '#00CED1', font_color = 'white')


            plt.show()
        else:
            os.system("clear")
            print('Encerrando Programa!')
            break

main()
