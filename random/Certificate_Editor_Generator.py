# import time
# import pyperclip
# import winsound
# import time
# import pyautogui
# data = []

# with open("data1.txt", "r") as file:
#     lines = file.readlines()
#     # print(lines)

# data = [line.strip() for line in lines]
# print(data)


# time.sleep(5)
# for name in data:
#     pyperclip.copy(name)
#     time.sleep(0.3)
#     pyautogui.moveTo(1169, 564, duration=0.3)
#     pyautogui.doubleClick()
#     pyautogui.hotkey('ctrl', 'a')
#     time.sleep(0.3)
#     pyautogui.hotkey('ctrl', 'v')
#     # print(pyautogui.position())

#     pyautogui.moveTo(970, 309, duration=0.3)
#     pyautogui.doubleClick()
#     pyautogui.hotkey('ctrl', 'a')
#     time.sleep(0.3)
#     pyautogui.hotkey('ctrl', 'v')

#     pyautogui.moveTo(1460, 306, duration=0.3)
#     pyautogui.click()
#     time.sleep(3)
#     print(pyautogui.position())


# for i in data:
#     if i not in new_data:
#         new_data.append(i)

# print(len(new_data))

# for line in new_data:
#     words = line.split()
#     with open("data.txt", "a") as file:
#         for word in words:
#             file.write(f"{word.capitalize()} ")

#         file.write("\n")

# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 300  # Set Duration To 1000 ms == 1 second


# with open("data.txt", "a") as file:
#     for line in new_data:
#         # for i in line.title():
#         file.write(f"{line}\n")

# for line in lines:
#     print(line.strip())
#     pyperclip.copy(line.strip())
#     time.sleep(15)


# time.sleep(10)
# for i in range(15):
#     x = 611
#     print(pyautogui.position())
#     pyautogui.moveTo(x, 890, duration=1)
#     pyautogui.click()
#     for j in range(13):
#         time.sleep(1)
#         pyautogui.moveTo(1207, 517, duration=0.3)
#         pyautogui.doubleClick()
#         pyautogui.hotkey('ctrl', 'a')
#         pyautogui.hotkey('ctrl', 'c')

#         pyautogui.moveTo(x, 940, duration=0.3)
#         time.sleep(1)
#         pyautogui.doubleClick()
#         time.sleep(5)

#         x += 100
#         pyautogui.moveTo(x, 890, duration=0.3)
#         time.sleep(1)
#         pyautogui.click()

#         winsound.Beep(frequency, duration)


# time.sleep(5)

# x += 91
# time.sleep(1)
# print(pyautogui.position())
# pyautogui.moveTo(x, 890, duration=1)
# time.sleep(5)
# print(pyautogui.position())
# # pyautogui.moveTo(702, 890, duration=1)
