import congrencialrandom as crand
import randu
import matplotlib.pyplot as plt
import random as rand
import entropygenerator as erand
import stats
from mpl_toolkits import mplot3d

# a = 45
# c = 1
# M = 1024

crand.seed(erand.rand())
# crand.seed(1000)
# randu.seed(erand.rand())
rand = [crand.rand() for i in range(500_001)]
# rand = [randu.rand() for i in range(500_001)]

ax = plt.axes(projection='3d')
ax.plot3D(rand[::3], rand[1::3], rand[2::3], 'ro', markersize=1)
# plt.title('randu')
# plt.title('X(n) = (' + str(a) + ' * X(n-1) + ' + str(c) + ') % ' +str(M))
plt.show()

print(stats.cov(rand[::2], rand[1::2]))
print(stats.var(rand))
print(stats.media(rand))
print(stats.chisq(rand))