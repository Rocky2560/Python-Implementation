
a = [1,2,3,4,5]
b = [1,6,7,8,5]
c = []
for i in a:
    for j in b:
        if i==j:
            c.append(i)

print(c)