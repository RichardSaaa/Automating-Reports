import pandas as pd
import pyautogui
import time
import pyperclip

#Primeira Fase > Abrir o Chrome
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(3)

#Segunda Fase > Abrir E-mail
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://drive.google.com")
pyautogui.press("enter")

time.sleep(3)

#Terceira Fase > Fazer Dowload do arquivo

pyautogui.click(x=393, y=98)
pyautogui.write("Compras.csv")
pyautogui.press("enter")
time.sleep(8)

clique = pyautogui.click(x=393, y=398)
for clique in range(3):
    clique = pyautogui.click(x=393, y=398)

pyautogui.click(x=1155, y=196)
pyautogui.click(x=951, y=599)

time.sleep(3)

#Quarta Fase > Lendo o Arquivo e somando

tabela = pd.read_csv("Compras.csv", sep=";")
print(tabela)

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

time.sleep(3)

#Quinta Fase > Enviando E-mail

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=74, y=168)

#Escrevendo o e-mail

time.sleep(5)
pyautogui.click(x=857, y=281)
pyautogui.write("seuemail@gmail.com")
time.sleep(3)

pyautogui.click(x=803, y=324)
pyautogui.write("Relatorio do dia")
pyautogui.hotkey("tab")

#Escrita do e-mail
text = f""""
Prezados clientes,

Segue o e-mail com o relatório de compras:

Total de Compras: {total_gasto:,.2f}
Quantidade de Produto: {quantidade:,.2f}
Preço Médio: {preco_medio:,.2f}

Att - Richard Alves Santos
"""

pyperclip.copy(text)
pyautogui.hotkey("ctrl", "v")

#Enviar e-mail

pyautogui.hotkey("ctrl", "enter")
