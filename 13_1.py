import numpy as np

aList = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
    [16, 17, 18, 19],
    [20, 21, 22, 23],
]
b = np.array(aList)
print(b.ravel())
print(b)

print('*' * 30)

print(b.flatten())
print(b)

print('*' * 30)

b.shape = (6, 4)
print(b)

print('*' * 30)
print(b.transpose())
print(b)

print('*' * 30)
print(b.reshape(2, 12))
print(b)
print('*' * 30)
print(b.resize(2, 12))
print(b)
