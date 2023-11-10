import pyautogui as py
from time import sleep
import subprocess

# Caminho para o executável do Google Chrome no Windows 10
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Comando para abrir o Chrome maximizado 
comando = f'"{chrome_path}" --start-maximized'
subprocess.Popen(comando, shell=True)

sleep(5)
py.click(227, 55, duration=1)
py.typewrite('outlook.com', interval=.1)
py.press('enter')
sleep(15)

emails = {'ptrk2511@gmail.com':['ENVIO DE EMAIL AUTOMATICO 1' , 'email automatico em python com pyautogui.'],
     'patrickrodriguez8620@gmail.com':['ENVIO DE EMAIL AUTOMATICO 2', 'email automatico em python com pyautogui.']}

t1 = 2
t2 = 5 

for key, value in emails.items():

    py.click(133,213, duration=1)
    sleep(t1 + 1)
    py.click(743, 357, duration=1)
    sleep(t1)
    py.typewrite(key, interval=.1)
    

    py.click(649,404, duration=1)
    py.typewrite(value[0], interval=.2)

    py.click(785,486, duration=1)
    sleep(t1)
    py.typewrite(value[1], interval=.2)

    py.click(689,296, duration=1)
    sleep(5)

py.hotkey('ctrl', 'w')




