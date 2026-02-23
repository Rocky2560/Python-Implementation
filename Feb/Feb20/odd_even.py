a = 2
if (a % 2 == 0):
    print(a,"is even")
else:
    print(a,"is odd")


num = [1,2,3,4,5]
total = 0
for i in num:
    if i % 2 == 0:
        total = total + i
print(total)

import logging
logging.basicConfig(level=logging.DEBUG)

import time
currentTime = time.localtime(time.time());
print("curent Time is ",currentTime)