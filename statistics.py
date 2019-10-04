def media(X):
    sum=0
    for i in range(len(X)):
        sum += X[i]
    
    return sum/len(X)


def var(X, sample=True):
    sum = 0
    avg = media(X)
    for i in range(len(X)):
        sum += (X[i] - avg)**2
        
    return sum/len(X-1) if sample else sum/len(X)
 
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