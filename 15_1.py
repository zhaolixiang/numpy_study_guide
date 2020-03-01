import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
print(np.hsplit(a, 3))
print(a)

print('*' * 30)

print(np.split(a, 3, axis=1))
print(a)

print('*' * 30)

a = np.arange(9).reshape(3, 3)
print(a)
print(np.vsplit(a, 3))

print('*' * 30)

a = np.arange(9).reshape(3, 3)
print(a)
print(np.split(a, 3, 0))

print('*' * 30)

c = np.arange(27).reshape(3, 3, 3)
print(c)
print('*' * 30)
print(np.dsplit(c, 3))
