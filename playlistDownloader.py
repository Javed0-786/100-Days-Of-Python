import pyautogui
import time

# print(pyautogui.size())
# pyautogui.moveTo(150, 150, duration=1)
# pyautogui.moveRel(0, 50, duration=1)
# moving to the position of top video link

# pyautogui.click(100, 100)
# time.sleep(1)
# pyautogui.scroll(-115)
# x, y = pyautogui.position()
# print(x, y)


# pyautogui.moveTo(1222, 389, duration=1)

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# the main program starts here

pyautogui.click(1170, 1041)  # open chrome
time.sleep(0.5)


pyautogui.click(84, 12)  # corner tab

pyautogui.moveTo(1137, 241, duration=0.5)
pyautogui.click(button='right')  # clicking right mouse button for the menu
time.sleep(0.5)
pyautogui.click(1222, 389)  # clicking on to the copy link option
time.sleep(0.5)
pyautogui.click(380, 12)  # side tab
time.sleep(0.5)
pyautogui.click(624, 445)  # paste the link to the bar available
pyautogui.hotkey("ctrlleft", "v")
time.sleep(0.5)
pyautogui.click(957, 749)  # to start the download


for i in range(1, 10):

    pyautogui.click(84, 12)  # corner tab
    time.sleep(0.5)

    # moving to the position of top video link
    pyautogui.moveTo(1137, 241, duration=0.5)
    time.sleep(0.5)
    pyautogui.scroll(-122)  # scrolling to move the video
    time.sleep(2)
    pyautogui.click(button='right')  # clicking right mouse button for the menu
    time.sleep(0.5)

    pyautogui.click(1222, 389)  # clicking on to the copy link option
    time.sleep(0.5)

    pyautogui.click(380, 12)  # side tab
    time.sleep(0.5)

    pyautogui.click(624, 445)  # paste the link to the bar available
    pyautogui.hotkey("ctrlleft", "v")
    time.sleep(7)

    pyautogui.click(957, 749)  # to start the download

print("Downloaded Succesfully")
