class Entropy:
    @staticmethod
    def rand():
        '''
            Generates a random int using the /dev/urandom file.
        '''
        path = '/dev/urandom'
        with open(path,'rb') as f:
            buffer = f.read(8)
            n = int.from_bytes(buffer, 'little')
        return n

prev: int

class Congrencial:
    @staticmethod
    def seed(X=None):
        global prev
        prev = X if X is not None and X > 0 else Entropy.rand()
        
        for _ in range(10): #Used to remove the initial bias of the Congrencial generator
            Congrencial.rand()

    @staticmethod
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

Congrencial.seed()

if __name__ == "__main__":
    pass