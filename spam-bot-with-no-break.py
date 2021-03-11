# script is importing pyautogui and time
import pyautogui
import time

time=0
# script what is changing the number in time thing
while time !=3:
    time +=1
    print("3 sekundy przerwy przed zaczeciem spamu")
    time.sleep(1)
# def of spam() thing
def spam(wiadomosc,ilosc):
    licznik=0
    while licznik !=ilosc:
        licznik +=1
        print("message has been wroted for" str(licznik) + "st time")
        pyautogui.write(wiadomosc)
        pyautogui.press("enter")

spam("example",20)

