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