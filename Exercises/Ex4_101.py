import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

x = np.array([0.83, 0.88, 0.88, 1.04, 1.09, 1.12, 1.29, 1.31,
              1.48, 1.49, 1.59, 1.62, 1.65, 1.71, 1.76, 1.83])
n = len(x)
ii = np.arange(1, n + 1)
pers = (ii - 0.50) / n

plt.figure()
# plt.plot(np.sort(x), stats.norm.ppf(pers,0,1), 'o')
plt.scatter(stats.norm.ppf(pers, 0, 1), np.sort(x))
plt.xlabel('Coating thickness', fontsize=14)
plt.ylabel('$z$ percentile', fontsize=14)
plt.show()

plt.figure()
stats.probplot(x, plot=plt)
plt.show()

#tmp = np.arange(1,7)
#x = np.tile(tmp,(6,1))
#y = x.transpose()
#pxy =np.array([[0.01,0.04,0.05,0.03,0.0,0.0],
#[0.01,0.04,0.11,0.06,0.0,0.0],
#[0.01,0.04,0.08,0.08,0.02,0.0],
#[0.0,0.03,0.07,0.06,0.04,0.0],
#[0.0,0.01,0.03,0.06,0.05,0.01],
#[0.0,0.0,0.01,0.02,0.02,0.01]])
#sum(sum(abs(x-y)*pxy))


tmp  = np.arange(0, 16, 5)
x    = np.tile(tmp[:-1], (len(tmp)-1, 1))
y    = np.tile(tmp, (len(tmp), 1)).transpose()
p_xy = np.array([[.02, .06, .02, .10],
                 [.04, .15, .20, .10],
                 [.01, .15, .14, .01]])
sum(sum((x + y) * p_xy))
