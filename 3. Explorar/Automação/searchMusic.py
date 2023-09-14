import pyautogui as pyt
from time import sleep
import subprocess
# Caminho para o executável do Google Chrome no Windows 10
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Comando para abrir o Chrome maximizado
comando = f'"{chrome_path}" --start-maximized'
subprocess.Popen(comando, shell=True)

sleep(5)
pyt.click(227, 55, duration=1)
sleep(1)
pyt.typewrite('www.youtube.com', interval=.1)
pyt.press('enter')
sleep(4)
pyt.click(397, 136,  duration=1)
sleep(1)
pyt.typewrite('sinais sorriso maroto', interval=.1)
pyt.press('enter')
sleep(3)
pyt.click(438, 306,  duration=1)