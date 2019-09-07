import entropygenerator as erand
prev = erand.rand()

def seed(x):
    global prev
    prev = x


def rand(a=16807, c=0, M=2**(32-1)-1):
    '''
        Generates a random number, where X(0) is the seed used.
        a is a multiplier between 1 and M
        c is an increment
        M is the greatest machine number
        X(n) = (a X(n-1) + c) % M
    '''
    global prev
    prev = ((a*prev+c) % M)
    
    return prev/M