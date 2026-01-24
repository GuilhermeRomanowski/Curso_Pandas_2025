#%% 
import pandas as pd
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
df = pd.read_html(url)
len(df)
type(df)
df_uf = df[1]

df_uf.to_csv("uf_wikipedia", sep = ";", index = False)
#Código georu erro 403 - Wikipedia está bloqueando a requisição.
#Isso da pra driblar utilizando o requests fingindo ser um agente de verdade, porém não é o tema do curso.
#Será visto durante estudo de requests.

# %%
