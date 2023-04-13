
from audioop import minmax
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_no = min(arr)
    max_no = max(arr)
    min_sum = sum(arr) - max_no
    max_sum = sum(arr) - min_no
    print(min_sum, max_sum)

if __name__ == '__main__':

    #Test Case 1 
    stdinp1 = [1,2,3,4,5]
    miniMaxSum(stdinp1)

    #Test Case 2 
    stdinp2 = [7,69,2,221,8974]
    miniMaxSum(stdinp2)
    #arr = list(map(int, input().rstrip().split()))

    #miniMaxSum(arr)
