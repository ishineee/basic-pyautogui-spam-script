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
    breakthing = 0
    if count == 5 or count == 5*2 or count == 5*3:
      while breakthing !=4:
        breakthing +=1
        print("break for " + str(breakthing) + "/4")
        sleep(1)

spam("your msg",20)
