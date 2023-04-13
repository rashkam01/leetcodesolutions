#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr,n):
    # create frequency list with initailized value of 0
    freq_list = [0]*(n)
    for i in range(0,len(arr)):
        # increment frequency list by 1 for every occurance of number in arr 
        freq_list[arr[i]] +=1
    return freq_list 

if __name__ == '__main__':

    arr = [1,1,3,2,1,7]
    n = max(arr)+1
    result = countingSort(arr,n)
    print(result)


