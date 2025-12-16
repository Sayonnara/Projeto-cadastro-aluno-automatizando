"""

name -999,291
email - 980,335
btn- 1034, 378

"""

import pyautogui
from time import sleep

with open ("alunos.txt", "r", encoding="utf-8") as file:
   for line in file:
      nome=line.split(",")[0]
      email=line.split(",")[1]
      pyautogui.click(999,291, duration=0.7)
      pyautogui.write(nome, interval=0.1)
      pyautogui.click(980,335, duration=0.7) 
      pyautogui.write(email, interval=0.1)
      pyautogui.click(1034,378, duration=0.7)   
     # pyautogui.screenshot(f"img/{nome}.png")
      sleep(2)

