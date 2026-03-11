a = '66';           print(int(a))
str = 'sudip manandhar'
print(str.split(" "))

list = [1,2,3,4]
list.remove(2)
list.pop(0)
print(list)
list.clear()
print(list)

import numpy as np
arr = np.array([1,2,3,4])
arr2 = np.flip(arr)
arr3 = arr[::-1]
print(arr2)
print(arr3)
print(arr[0])
arr[2] = 6
x = np.delete(arr,0)
print(x)

st1 = ['W', 'a', 'w', 'b']
lst2 = ['e', 're', 'riting', 'log']
list3 = [x + y for x,y in zip(st1,lst2)]
print(list3)
num = [1,2,3]
sq =[]
for x in arr.tolist():
    sq.append(x*x)
print(sq)

a = 'this is a good day'
li = a.split(' ')
print(li)
jo = ' '.join(li)
print(jo)
from math import sqrt;
def prime(x):
    for i in range(2, int(sqrt(x))+1):
        if (x%i==0):
            return False
    return True
print(prime(5))

a=5
b=10
temp =a
a=b
b=temp
a,b = b,a
print(a)
print(b)
from math import factorial
def factorials(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
print(factorials(5))
print(factorial(5))

from functools import reduce
x=[1,2,5,3]
y=[1,2,5,3]
ch = ['a','b','c','d']
print(','.join(ch))
# reduce(lambda x,y: x if x<y else y,b)

print([i for i in range(1,10) if i%2 != 0])

c = np.concatenate((arr,arr2,arr3), axis=0)
print(c)