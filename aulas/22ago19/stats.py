def media(X):
    sum=0
    for i in range(len(X)):
        sum += X[i]
    
    return sum/len(X)


def var(X):
    sum = 0
    avg = media(X)
    for i in range(len(X)):
        sum += (X[i] - avg)**2
        
    return sum/len(X)
 
def desvp(X):
    return var(X)**(1/2)

def cov(X, Y):
    if len(X) != len(Y): return None
    
    sum = 0
    avgX = media(X)
    avgY = media(Y)
    for i in range(len(X)):
        sum += (X[i] - avgX)*(Y[i] - avgY)

    return sum/(len(X) - 1)

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

def chisq(X, n_div=10):
    n = len(X)
    exp = n / n_div

    obs = [0 for i in range(n_div)]

    for i in X:
        obs[int(i*n_div)] += 1

    chi = 0
    for i in range(n_div):
        chi += (obs[i] - exp)**2

    return chi/exp
    