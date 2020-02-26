import sys
from datetime import datetime
import numpy as np

"""

本书第1章 该段代码演示Python中的向量加法 使用如下命令运行程序：

python vectorsum.py n

n为指定向量大小的整数

加法中的第一个向量包含0到n的整数的平方 第二个向量包含0到n的整数的立方 程序将打印出向量加和后的最后两个元素以及运行消耗的时间 
"""


def pythonsum(n):
    a = [i for i in range(n)]
    b = [i for i in range(n)]
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c


def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c


if __name__ == '__main__':
    n = 3000
    start = datetime.now()
    c = numpysum(n)
    delta = datetime.now() - start
    print('最后两个数', c[-2:])
    print('delta', delta)

    print('*' * 20)

    start = datetime.now()
    c = pythonsum(n)
    delta = datetime.now() - start
    print('最后两个数', c[-2:])
    print('delta', delta)

