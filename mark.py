import numpy as np
a = []
b = []
x = 2.7
y = 2.7
for i in range(5):
    # x = x * 1.1
    # a.append(x)
    a.append(x*1.1**(i+1))

for i in range(5):
    # y = y * 0.9
    b.append(y*0.9)
print(a)
print(b)


