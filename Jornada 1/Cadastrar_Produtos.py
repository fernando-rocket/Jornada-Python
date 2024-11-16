# Código da Aula python2024

import pyautogui
from time import sleep
import pandas as pd

pyautogui.PAUSE = 0.5
link =  "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

tabela = pd.read_csv("produtos.csv")

# Abrindo o chrome e o link

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=620, y=620, clicks=1)
pyautogui.write(link)
pyautogui.press("enter")
sleep(1)
pyautogui.click(x=870, y=18)

# Fazendo login

pyautogui.click(x=695, y=477)
pyautogui.write("emailgenerico@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
sleep(1)

# Cadastrando o Produto
for linha in tabela.index:
    pyautogui.click(x=636, y=323)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    x = str(tabela.loc[linha, "obs"])
    if x == "nan":
        x = "Sem Obs"
    pyautogui.write(x)
    pyautogui.press("tab")
    pyautogui.press("enter")    
    pyautogui.scroll(5000)
    