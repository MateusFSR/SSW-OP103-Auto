import pyautogui as pa
import time
import keyboard

play = (1048, 308)
posiA1 = (72, 299)
boxTYPE = (923, 307)
list = (104, 853)

def bnu():
    pa.click(boxTYPE, clicks=2)
    pa.sleep(0.5)
    pa.write('BNU')


while True:
    #code
    pa.click(boxTYPE, clicks=2)
    pa.write('CWB')
    pa.sleep(2.0)
    pa.scroll(-300)
    botaox = pa.locateOnScreen('buttonx.png', confidence=0.8)

    if botaox:            
    # Obtenha as coordenadas do x
        x_pos, y_pos = pa.center(botaox)
    pa.moveTo(x_pos, y_pos)

    # copiar dados tabela
    pa.move(30, 0)
    pa.hotkey('ctrl', 'a')
    pa.keyDown('shift')
    pa.click()
    pa.keyUp('shift')
    pa.hotkey('ctrl', 'c')
    pa.sleep(1.3)
    pa.click(list)

    botaolistacwb = pa.locateOnScreen('cwbcolar.png', confidence=0.8)
    if botaolistacwb:            
    # Obtenha as coordenadas do x
        x_pos, y_pos = pa.center(botaolistacwb)
    pa.moveTo(x_pos, y_pos)
    pa.click()

    pa.sleep(1.0)
    pa.click(posiA1)
    pa.hotkey('ctrl', 'v')
    pa.sleep(0.6)
    pa.hotkey('alt', 'tab')
    pa.sleep(0.7)
    pa.press('esc')
    pa.sleep(2.0)

    #BNU

    bnu()
    pa.sleep(2.0)
    pa.scroll(-300)
    botaox = pa.locateOnScreen('buttonx.png', confidence=0.8)

    if botaox:            
    # Obtenha as coordenadas do x
        x_pos, y_pos = pa.center(botaox)
    pa.moveTo(x_pos, y_pos)

    # copiar dados tabela
    pa.move(30, 0)
    pa.hotkey('ctrl', 'a')
    pa.keyDown('shift')
    pa.click()
    pa.keyUp('shift')
    pa.hotkey('ctrl', 'c')
    pa.sleep(1.3)
    pa.click(list)

    botaolistabnu = pa.locateOnScreen('bnucolar.png', confidence=0.8)
    if botaolistabnu:            
    # Obtenha as coordenadas do x
        x_pos, y_pos = pa.center(botaolistabnu)
    pa.moveTo(x_pos, y_pos)
    pa.click()
    pa.sleep(1.0)

    pa.click(posiA1)
    pa.hotkey('ctrl', 'v')
    pa.sleep(0.6)
    pa.hotkey('alt', 'tab')
    pa.press('esc')
    pa.sleep(2.0)

    time.sleep(10)




