import pyautogui
import time
import pandas as pa


# pyautogui.click() - > clica
# pyautogui.write() - > escreve
# pyautogui.press() -> aperta tecla
# pyautogui.hotkey() -> atalho ( combinação de tecla)

pyautogui.PAUSE = 0.3

pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press('enter')

time.sleep(1)
#  x=542, y=587
pyautogui.click(x=711, y=584 ) # se por a propriedade clicks = 2 ele clica 2x

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(1)

email = "leo@hotmail.com"
senha = "12345"
pyautogui.click(x=623, y=397)
time.sleep(.5)
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('enter')

time.sleep(.7)
pyautogui.press('enter')
tabela = pa.read_csv("produtos.csv")

for linha in tabela.index: 
       
    
    pyautogui.click(x=626, y=285)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha,"obs"]
    if not pa.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("enter")   
    pyautogui.scroll(1000)