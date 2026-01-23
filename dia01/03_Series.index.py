#%%
import pandas as pd

idades = [32, 38, 30, 30, 31,
          35, 25, 29, 31, 37,
          27, 23, 36, 33, 39]

series_idades = pd.Series(idades)
series_idades

#%%
#Acessar primeiro elemento da lista
idades[0]
#Último elemento da lista
idades[-1]

#Como fazer a mesma coisa com a série?
#Primeiro elemento é igual a lista:
series_idades[0]


#Ordenando séries do menor pro maior, verifica que a linha permanece a mesma vinculada ao elemento:
series_idades = series_idades.sort_values()
series_idades

#Os índices da série funcionam da mesma maneira que uma chave no dicionário.
#Pra puxar o último elemento, é diferente da lista:
#utilizamos o iloc conseguimos utilizar pela posição:
series_idades.iloc[0] #primeira posição
series_idades.iloc[-1] #última posição

#O .iloc basicamente ignora as chaves e busca direto pelo elemento, como numa lista.
series_idades.iloc[:3]
series_idades.iloc[::-1] 

#%% Pordemos também setar os índices
idades = [32, 38, 30, 30, 31,
          35, 25, 29, 31, 37,
          27, 23, 36, 33, 39]

indexs = ["Teo", "Maria", "Jose", "Luis", "Ana",
          "Nah", "Dani", "Mah", "Fer", "Nanda",
          "Naty", "Nih", "Pedro", "Kozato", "Tito"]

series_idades = pd.Series(idades,index=indexs)
series_idades


# %%Assim as chaves passam a ser o nome do index.
series_idades["Teo"]
# E continuamos podendo trazer a posição utilizando o .iloc
series_idades.iloc[0]
# %%
import pandas as pd
idades = [32, 38, 30, 30, 31,
          35, 25, 29, 31, 37,
          27, 23, 36, 33, 39]

nomes = ["Teo", "Maria", "Jose", "Luis", "Ana",
          "Nah", "Dani", "Mah", "Fer", "Nanda",
          "Naty", "Nih", "Pedro", "Kozato", "Tito"]

Series_idades = pd.Series(idades)
Series_nomes = pd.Series(nomes)
