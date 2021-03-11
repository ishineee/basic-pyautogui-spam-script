# script is importing pyautogui and time
import pyautogui
import time

time=0
# script what is changing the number in time thing
while time !=3:
    time +=1
    print("3 sekundy przerwy przed zaczeciem spamu")
    time.sleep(1)
def spam(msg,maxmsg):
    licznik=0
    while licznik !=maxmsg:
        licznik +=1
        print("message has been wroted for" str(licznik) + "st time")
        pyautogui.write(msg)
        pyautogui.press("enter")
        # break thing
        if count == 5 or count == 5*2 or count == 5*3:
            sleep(4)

spam("example",20)

