import pyautogui
import time
msg = input("Mensagem: ")
n = input("Quantas Vezes?: ")
time.sleep(5)
for i in range(0,int(n)):
    pyautogui.typewrite(msg + '\n')