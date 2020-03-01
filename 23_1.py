import numpy as np

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
print('c=', c)
print('*' * 30)

print('np.diff(c)=', np.diff(c))
print('*' * 30)

returns = np.diff(c) / c[:-1]
print('returns=', returns)
print('*' * 30)
print('3.22/336.1=', 3.22 / 336.1)
print('*' * 30)

print('Standard deviation =', np.std(returns))

print('*' * 30)
logreturns = np.diff(np.log(c))
print('logreturns = ', logreturns)
print('*' * 30)

posretindices = np.where(returns > 0)
print('posretindices = ', posretindices)
print('*' * 30)

annual_volatility = np.std(logreturns) / np.mean(logreturns)
annual_volatility = annual_volatility / np.sqrt(1. / 252.)
print('annual_volatility = ', annual_volatility)
print('*' * 30)

print('Month volatility:', annual_volatility * np.sqrt(1. / 12.))
print('*' * 30)
print('*' * 30)
