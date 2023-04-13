#!/bin/python3



#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    pos_no = 0
    neg_no = 0 
    zero_no = 0 
    arr_length = len(arr)
    
    for x in range(arr_length):
        if (arr[x] > 0):
            pos_no = pos_no + 1
        elif (arr[x] < 0):
            neg_no = neg_no + 1 
        elif (arr[x] == 0):
            zero_no = zero_no + 1 
    print(pos_no/arr_length)
    print(neg_no/arr_length)
    print(zero_no/arr_length)
            

if __name__ == '__main__':

    # Test Case 1:
    a1 = [ -4, 3, -9, 0, 4, 1 ];
    plusMinus(a1);
 
    # Test Case 2:
    a2 = [ 1, 2, 3, -1,-2, -3, 0,0 ];
    plusMinus(a2);
    
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))

    #plusMinus(arr)