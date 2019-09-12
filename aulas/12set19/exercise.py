from mcinversetransform import *

class DistA:
    def x(self, rand=crand.rand):
        return sqrt(rand())

    def f(self, x):
        return 2*x 

if __name__ == "__main__":
    A = samplenumbers(DistA())
    plt.plot([x for x, _ in A], [y for _, y in A], 'k+', markersize=0.1)
    plt.show()
