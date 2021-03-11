import pyautogui
from time import sleep
time=0
while time !=3:
  time +=1
  print(str(time) + "/3 before script will starts spaming")
  sleep(1)
def spam(msg,quantity):
  count=0
  while count !=quantity:
    count +=1
    print(str(count) + "/" + str(quantity))
    pyautogui.write(msg)
    pyautogui.press("enter")
spam("your msg",20)
