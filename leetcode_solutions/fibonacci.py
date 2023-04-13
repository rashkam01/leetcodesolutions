
import numpy as np

def fibonacchi(N, a, b):
    L = []
    a , b = a, b
    while len(L) < N:
        a , b = b, a+b
        L.append(a)
    return L

if __name__ == '__main__':

    result = fibonacchi(10, 0, 1)
    print(result)