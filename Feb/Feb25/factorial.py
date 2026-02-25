def fact(n):
    if n == 0:
        return 1;
    else:
        return n * fact(n-1)

x = 3
print(fact(x))

# Largest Eleement in list#
def largest(num):
    largest = num[0]
    for i in num:
        if (i > largest):
            largest = i
    return largest

a = [1,2,5,8,3]
largets = largest(a)
print(largets)
