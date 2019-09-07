import congrencialrandom as crand
import entropygenerator as erand
import matplotlib.pyplot as plt
from math import log, exp, factorial, cos, sin, pi, sqrt

class Exponencial:
    def __init__(self, a=1):
        self.a = a

    def x(self, rand=crand.rand):
        return -log(1-rand())/self.a
    
    def f(self, x):
        return self.a*exp(-x*self.a)

class Uniform:
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b

    def x(self, rand=crand.rand):
        return (self.b-self.a)*rand() + self.a
    
    def f(self, x): 
        return 1/(self.b-self.a)

class Erlang:
    def __init__(self, a=1, k=5):
        self.a = a
        self.k = k

    def x(self, rand=crand.rand):
        def prod(rand):
            prod = 1
            for _ in range(self.k):
                prod *= rand()
            return prod

        return - log(prod(rand))/self.a

    def f(self, x): 
        return (self.a*exp(-self.a*x)*((self.a*x)**(self.k-1)))/factorial(self.k-1)

class Normal:
    def __init__(self, avg=0, std=1):
        self.avg = avg
        self.std = std

    def x(self, rand=crand.rand): 
        return sqrt(-2*log(rand())) * cos(2*pi*rand())
    
    def f(self, x): 
        return exp(-0.5*((x - self.avg)/self.std)**2) / sqrt(2*pi)*self.std

def samplenumbers(dist=Normal(), n = 100000):
    X = [dist.x() for _ in range(n)]
    Y = [dist.f(x) for x in X]
    return list(zip(X,Y))

if __name__ == "__main__":
    A = samplenumbers()
    plt.plot([x for x, _ in A], [y for _, y in A], 'k+', markersize=0.1)
    plt.show()