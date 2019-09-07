
def corr(X, Y):
    def raiscrt(X, sum_x, n):
        aux = 0
        for i in range(len(X)):
            aux += X[i]**2

        return (n * aux - sum_x**2 )**(1/2)

    if range(len(X)) != range(len(Y)): return None

    n = len(X)
    cor = 0
    sum_xy = 0
    sum_x = sum(X)
    sum_y = sum(Y)

    for i in range(n):
        sum_xy += X[i]*Y[i]

    cor = sum_xy*n - sum_x*sum_y
    cor /= raiscrt(X, sum_x, n)*raiscrt(Y, sum_y, n)

    return cor