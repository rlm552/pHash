def hammingDistance(h1, h2):    
    d = 0
    r = h1 ^ h2
    
    while r != 0:
        if r % 2 == 1:
            d += 1
        r = r >> 1
    return d

def hammingRatio(h1, h2, hash_size):
    d = hammingDistance(h1, h2)
    if d <= 5:
        return (True, d)
    else:
        return (False, d)


