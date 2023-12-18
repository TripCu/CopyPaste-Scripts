import pyautogui, time
time.sleep(5)
f = open("shrek.txt")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")