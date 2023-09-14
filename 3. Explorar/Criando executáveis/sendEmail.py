import pyautogui as py
from time import sleep
import subprocess

comando = "google-chrome --start-maximized"
subprocess.Popen(comando, shell=True )

sleep(4)
py.press('esc')
sleep(1)
py.doubleClick(228, 83)
sleep(1)
py.hotkey('ctrl', 'a') 
sleep(1) 
py.press('backspace')
sleep(1)
py.typewrite('outlook.com', interval=.2)
sleep(2)
py.press('enter')

sleep(6)

emails = {'ptrk2511@gmail.com':['ENVIO DE EMAIL AUTOMATICO 1' , 'email automatico em python com pyautogui.'],
     'patrickrodriguez8620@gmail.com':['ENVIO DE EMAIL AUTOMATICO 2', 'email automatico em python com pyautogui.']}

t1 = 2
t2 = 5 

for key, value in emails.items():

    py.click(108,217)
    sleep(t1 + 1)
    py.click(599, 308)
    sleep(t1)
    py.typewrite(key, interval=.1)
    

    py.click(535,349)
    py.typewrite(value[0], interval=.2)

    py.click(847,446)
    sleep(t1)
    py.typewrite(value[1], interval=.2)

    py.click(547,264)
    sleep(5)

py.hotkey('ctrl', 'w')




