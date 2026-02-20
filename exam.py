
from math import floor, ceil

a = [1,2,3]
b= [2,3,4]
print(a+b)
a.extend(b)
print(a)

c =3.1
print(floor(c))
print(ceil(c))

x=6
y=5
print(x/y)
print(x//y)


def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def appFunc(func, a,b):
    return func(a,b)
print(appFunc(sub, 3,4))


# ✅ Key Takeaways
#
# Numbers, strings, tuples → immutable → behave like call by value.
#
# Lists, dictionaries, sets → mutable → behave like call by reference.
#
# If you modify a mutable object inside a function, the original
# object outside the function also changes.

def call_by_val(x):
    return x*2

def call_by_ref(x):
    x.append("D")
    return x
b = ["E"]
a = 2

upated_num = call_by_val(a)
print(upated_num)

updated_list = call_by_ref(b)
print(updated_list)

s1= 'GeeksS'
s2 = lambda func: func.upper()
print(s2(s1))

a=[2,3,4,5]
res = [val ** 2 for val in a]
print(res)