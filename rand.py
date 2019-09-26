class Entropy:
    def rand():
        '''
            Generates a random number, between 0 and 1, using the /dev/random file.
        '''
        path = '/dev/random'
        with open(path,'rb') as f:
            buffer = f.read(8)
            n = int.from_bytes(buffer, 'little')
        return n / (2**64 - 1)

prev = entropyrandom.rand()

class Congrencial:
    def seed(x):
        global prev
        prev = x


    def rand(a=16807, c=0, M=2**(32-1)-1):
        '''
            Generates a random number, between 0 and 1, where X(0) is the seed used.
            a is a multiplier between 1 and M
            c is an increment
            M is the greatest machine number
            X(n) = (a X(n-1) + c) % M
        '''
        global prev
        prev = ((a*prev+c) % M)
        
        return prev/M
