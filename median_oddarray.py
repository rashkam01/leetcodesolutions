import sys
import numpy as np
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def medianofarray(arr):
    x = np.sort(arr)
    length_array = len(arr)
    median_pos = length_array // 2 
    print(median_pos)
    median = x[median_pos]
    return median

if __name__ == '__main__':

    #Test Case 1 
    stdinp1 = [2,1,5,4,3,8,9,11,13]
    result = medianofarray(stdinp1)
    print(result)
