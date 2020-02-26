import numpy as np

b = np.arange(24).reshape(2, 3, 4)
print(b.shape)
print(b)

print(b[0][0][0])

print('*' * 30)

print(b[:, 0, 0])
print('*' * 30)
print(b[0])

print('*' * 30)

print(b[0, :, :])

print('*' * 30)

print(b[0, ...])

print('*' * 30)

print(b[0, 1])

print('*' * 30)
print(b[0, 1, ::2])

print('*' * 30)
print(b[..., 1])
print('*' * 30)
print(b[:, 1])
print('*' * 30)
print(b[0, :, 1])
print('*' * 30)
print(b[0, :, -1])
print('*' * 30)
print(b[0, ::-1, -1])
print('*' * 30)

print(b[0, ::2, -1])
print('*' * 30)

print(b[::-1])
print('*' * 30)
