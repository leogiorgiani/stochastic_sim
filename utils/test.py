from Distributions import Erlang
from Random import Congrencial as crand

crand.seed(1000)
g = Erlang(1.5, 4)

A = [g.x() for _ in range(100)]

print(A)

