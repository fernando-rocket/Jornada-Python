import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)
print(tabela['marca'][0])