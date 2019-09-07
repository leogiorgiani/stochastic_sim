prev = 3

def seed(x):
    global prev
    prev = x

def rand():
    '''
      Randu pseudorandom generator:
      X(n) = ((2**16+3) * X(n-1)) % 2**(32-1)
    '''
    global prev
    prev = ((2**16+3) * prev) % 2**(32-1)

    return prev / (2**(32-1))