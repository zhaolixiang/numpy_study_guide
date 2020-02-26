import numpy as np

t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
print(t)

print(t['name'])

item = np.array([('DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
print(item[1])
