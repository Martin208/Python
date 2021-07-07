import time
import os

count_mins = int(input('How much time do you need? '))
sec=0
mins=0
while sec<=60:
    os.system('clear')
    print(f'{mins} minutes  {sec} seconds')
    time.sleep(1)
    sec+=1
    if sec==60:
        mins+=1
        sec=0
if mins == count_mins:
    print('Stop the clock!')
    exit()
print('Thanks for using this counter!')