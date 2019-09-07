import entropygenerator as erand
import congrencialrandom as crand
import random as rand
import matplotlib.pyplot as plt
from math import sin, sinh, cosh

def integrate(f, randn=100000, A=None, S=1):
    if A is None:
        crand.seed(erand.random())
        A = [(crand.random(), crand.random()) for i in range(randn)]
    
    n=0
    for x, y in A:
        if y <= f(x):
            n+=1

    return (n/len(A))*S

if __name__ == "__main__":
    def fa(x): return sin(x)*cosh(x)

    def fb(x): return sin(x)*sinh(x)

    def circ(x): return (1-x**2)**(1/2)
        
    s=1.3

    crand.seed(erand.random())
    A = [(crand.random(), s*crand.random()) for _ in range(1000000)]

    print("a: ", integrate(fa, A=A, S=s))
    print("b: ", integrate(fb, A=A, S=s))
    print("pi:", 4*integrate(circ, A=A, S=s))

    f=fa

    plt.plot([x for x, y in A if y>f(x)], [y for x, y in A if y>f(x)], 'b+', markersize=0.1)
    # plt.plot([x for x, _ in A], [f(x) for x,_ in A], 'ko', markersize=0.1)
    plt.plot([x for x, y in A if y<=f(x)], [y for x,y in A if y <= f(x)], 'r+', markersize=0.1)
    plt.axes().set_aspect('equal')
    plt.show()