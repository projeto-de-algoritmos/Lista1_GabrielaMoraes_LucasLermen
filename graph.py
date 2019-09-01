import pandas as pd
import json
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

    listaAeroportos = sorted((set(listaEstacoes)))

    # Salvando lista de adjacência
    with open('listaAdjacencia.json', 'w') as json_file:
        json.dump(listaDeAdjacencia, json_file)
    
    # print(listaDeAdjacencia)
    print(BFS(listaDeAdjacencia, 'campo-limpo', 'largo-treze'))
main()
