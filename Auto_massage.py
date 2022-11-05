import pyautogui
import time
print('write your massage here')
y = input()
print('How many times would you like to send this massage to your dear persion? as an example: 10')
z = 1
x = float(input())
print("It will start under 5sec, so make sure you're in the right place for send massages")
time.sleep(5)
while z <= x:
	pyautogui.write(y, interval=0.001)
	pyautogui.press('enter')
	z = z+1
