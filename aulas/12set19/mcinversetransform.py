import congrencialrandom as crand
import entropyrandom as erand
import matplotlib.pyplot as plt
from math import log, exp, factorial, cos, sin, pi, sqrt, floor

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

class Geometric:
    def __init__(self, p=0.5, q=0.5):
        if p+q != 1:
            raise Exception("p+q has to be equal 1, but is equal to {}".format(p+q))
        self.p = p
        self.q = q

    def x(self, rand=crand.rand):
        return floor((log(rand())/log(1-self.p)) + 1)

    def f(self, x):
        # return 1 - self.q**(x+1) #accumulate function
        return self.p * self.q**(x - 1)

class Poisson:
    def __init__(self, lamb = 0.5):
        self.lamb = lamb
    
    def x(self, rand=crand.rand):
        prod = 1
        i = 0 
        explamb = exp(-self.lamb)
        while prod >= explamb:
            prod *= rand()
            i+=1

        return i

    def f(self, x):
        return (self.lamb**x * exp(-self.lamb)) / factorial(x)

class Weibul:
    def __init__(self, a=2, b=1):
        self.a = a
        self.b = b

    def x(self, rand=crand.rand):
        return self.b * (- log(rand()))**(1/self.a)

    def f(self, x):
        return self.a * self.b**(-self.a) * x**(self.a-1) * exp(-(x/self.b)**self.a)

def samplenumbers(dist=Normal(), n = 100000):
    X = [dist.x() for _ in range(n)]
    Y = [dist.f(x) for x in X]
    return list(zip(X,Y))

if __name__ == "__main__":
    A = samplenumbers(Weibul(a = 1.5, b=3),10000)
    for x, y in A:
        print("({}, {})".format(x,y))
    plt.plot([x for x, _ in A], [y for _, y in A], 'k+', markersize=0.1)
    plt.show()

