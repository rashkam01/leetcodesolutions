#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    # Write your code here
    # Initialize sums of diagonals
    d1 = 0
    d2 = 0
 
    for i in range(0, n):
     
        for j in range(0, n):
         
            # finding sum of primary diagonal
            if (i == j):
                d1 += arr[i][j]
 
            # finding sum of secondary diagonal
            if (i == n - j - 1):
                d2 += arr[i][j]
    print(d1)
    print(d2)     
    # Absolute difference of the sums
    # across the diagonals
    return abs(d1 - d2)

if __name__ == '__main__':


    n = 3

    arr = [[1,2,3],[4,5,6],[9,8,9]]


    result = diagonalDifference(arr, n)
    print(result)