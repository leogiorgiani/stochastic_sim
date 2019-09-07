import entropygenerator as erand
import congrencialrandom as crand
import matplotlib.pyplot as plt

crand.seed(erand.random())

A = [(crand.random(), crand.random()) for i in range(500000)]

n=0
for x, y in A:
    if ((x**2 + y**2) <= 1):  # X² + Y² ≤ 1
        n+=1

pi = 4 * (n/(len(A)))

print(pi)