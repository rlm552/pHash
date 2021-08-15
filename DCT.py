import numpy as np

def alpha(sf):
    if sf == 0:
        return 1/np.sqrt(2)
    return 1

def doubleSum(u, v, matrix):
    sum = 0
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]
    
    for x in range(num_rows):
        for y in range(num_cols):
            sum += matrix[x][y] * np.cos(((2*x + 1) * u * np.pi)/16)*np.cos(((2*y + 1) * v * np.pi)/16)
    
    return sum
    
def DCT(matrix):
    dct_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
    num_rows = dct_matrix.shape[0]
    num_cols = dct_matrix.shape[1]
    
    for u in range(num_rows):
        for v in range(num_cols):
            dct_matrix[u][v] = 1/4 * alpha(u) * alpha(v) * doubleSum(u, v, matrix)
    
    return dct_matrix
'''
g = np.array([[-76, -73, -67, -62, -58, -67, -64, -55],
              [-65, -69, -73, -38, -19, -43, -59, -56],
              [-66, -69, -60, -15, 16, -24, -62, -55],
              [-65, -70, -57, -6, 26, -22, -58, -59],
              [-61, -67, -60, -24, -2, -40, -60, -58],
              [-49, -63, -68, -58, -51, -60, -70, -53],
              [-43, -57, -64, -69, -73, -67, -63, -45],
              [-41, -49, -59, -60, -63, -52, -50, -34]])

np.set_printoptions(precision=2, suppress = True)
print(DCT(g))
'''