import random
import pyautogui as pg
import time

msg=["@ayush","@nishant","@yash"]
time.sleep(8)


for i in range(200):
    a = random.choice(msg)
    pg.write(a)
    pg.press("enter")