#!/bin/python3

import math
import os
import numpy as np 
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    r=a[0]
    #print(r)
    n = len(a)
    #print(n)
    for i in range(1,n):
        print('a[i]', a[i])
        print(format(a[i], 'b'))
        print('r', r)
        print(format(r,'b'))
        r = r^a[i]
        print('changed R', r)
        print('next')
    return r

if __name__ == '__main__':

    a = [4,5,5]
    result = lonelyinteger(a)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
