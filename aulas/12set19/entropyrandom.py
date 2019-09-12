def rand():
    path = '/dev/random'
    with open(path,'rb') as f:
        buffer = f.read(8)
        n = int.from_bytes(buffer, 'little')
    return n / (2**64 - 1)