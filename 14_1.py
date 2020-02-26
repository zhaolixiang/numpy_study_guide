import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)

b = 2 * a
print(b)

print('*' * 30)

print(np.hstack((a, b)))

print('*' * 30)

print(np.concatenate((a, b), axis=1))

print('*' * 30)

print(np.vstack((a, b)))

print('*' * 30)

print(np.concatenate((a, b), axis=0))

print('*' * 30)

print(np.dstack((a, b)))

print('*' * 30)

oned = np.arange(2)
print(oned)
twice_oned = 2 * oned
print(twice_oned)
print(np.column_stack((oned, twice_oned)))

print('*' * 30)

a = np.arange(9).reshape(3, 3)
print(a)
b = 2 * a
print(b)
print(np.column_stack((a, b)))
print(np.column_stack((a, b)) == np.hstack((a, b)))

print('*' * 30)

oned = np.arange(2)
print(oned)
twice_oned = 2 * oned
print(twice_oned)
print(np.row_stack((oned, twice_oned)))

print('*' * 30)

a = np.arange(9).reshape(3, 3)
print(a)
b = 2 * a
print(b)
print(np.column_stack((a, b)))
print(np.row_stack((a, b)) == np.vstack((a, b)))
