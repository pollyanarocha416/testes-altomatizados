import pyautogui

#area de trabalho
#pyautogui.hotkey('winleft', 'd')



# checar email:

#pos = pyautogui.position() # descobrir a posicao
#print(pos)


#funcao de checar e-mail:
def checar_email():
    pyautogui.moveTo(x=1055, y=1059)
    pyautogui.PAUSE = 1.5
    pyautogui.click()
#checar_email()

def tirar_print():
    pyautogui.moveTo(x=1160, y=1070)
    pyautogui.PAUSE = 2.0
    pyautogui.click()

    pyautogui.moveTo(x=35, y=51)
    pyautogui.PAUSE = 1.0
    pyautogui.click()

    pyautogui.mouseDown()#segurar
    pyautogui.PAUSE = 1.0
    pyautogui.moveTo(x=1905, y=1028)
    pyautogui.mouseUp()#soltar
tirar_print()

pos = pyautogui.position() # descobrir a posicao
print(pos)