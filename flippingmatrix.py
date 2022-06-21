#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(a):
        suma = 0 
        n=2 
        for i in range(n):
            for j in range(n):
                #print(a[i][j],a[2*n-i-1][j])
                #print(a[i][2*n-j-1],a[2*n-i-1][2*n-j-1])
                #print((max(a[i][j],a[2*n-i-1][j]),max(a[i][2*n-j-1],a[2*n-i-1][2*n-j-1])))
                #print(max(max(a[i][j],a[2*n-i-1][j]),max(a[i][2*n-j-1],a[2*n-i-1][2*n-j-1])))
                suma += max(max(a[i][j],a[2*n-i-1][j]),max(a[i][2*n-j-1],a[2*n-i-1][2*n-j-1]))
                #print(a[i][j])
        return(suma)

if __name__ == '__main__':

    matrix = [[112,42,83,119], \
               [56,125,56,49], \
               [15,78,101,43], \
               [62,98,114,108]]

    result = flippingMatrix(matrix)
    print(result)
