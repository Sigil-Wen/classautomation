import time
import pyautogui 
currentMouseX, currentMouseY = pyautogui.position() 
pyautogui.FAILSAFE = False
def openChrome(link):
    screenWidth, screenHeight = pyautogui.size() 
    
    pyautogui.press('win', interval = 1)
    pyautogui.write('Chrome', interval=0.1)
    pyautogui.press('enter', interval = 1)
    pyautogui.write(link + '', interval=0.1)
    pyautogui.press('enter')
link = 'https://meet.google.com/jmw-wzxh-tsr'
openChrome(link)

def login():
    pyautogui.moveTo(1269, 582)
    pyautogui.click()


time.sleep(5)












