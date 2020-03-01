import numpy as np

b = np.arange(24).reshape(2, 12)
print(b)
print(b.ndim)

print('*' * 30)

b = np.arange(24).reshape(2, 12)
print(b)
print(b.size)

print('*' * 30)

b = np.arange(24).reshape(2, 12)
print(b)
print(b.itemsize)

print('*' * 30)

b = np.arange(24).reshape(2, 12)
print(b)
print(b.nbytes)

print('*' * 30)
b = np.arange(24).reshape(2, 12)
print(b)
print('*' * 30)
b.resize(6, 4)
print(b)
print('*' * 30)
print(b.T)

print('*' * 30)
b = np.arange(5)
print(b)
print(b.ndim)
print(b.T)

print('*' * 30)

b = np.array([1.j + 1, 2.j + 3])
print(b)

print('*' * 30)
b = np.array([1.j + 1, 2.j + 3])
print(b)
print(b.real)

print('*' * 30)
b = np.array([1.j + 1, 2.j + 3])
print(b)
print(b.imag)

print('*' * 30)
b = np.array([1.j + 1, 2.j + 3])
print(b.dtype)
print(b.dtype.str)

print('*' * 30)
b = np.arange(4).reshape(2, 2)
print(b)
f = b.flat
print(f)
for item in f:
    print('item', item)

print(b.flat[2])
print(b.flat[[1, 3]])

b.flat = 7
print(b)

# or selected elements
b.flat[[1, 3]] = 1
print(b)
