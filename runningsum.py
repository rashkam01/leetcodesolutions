'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

'''


def runningsum(mylist = []):
    a = []
    x = 0 
    for i in mylist:
        x = x + i 
        a.append(x)
    return a 


if __name__ == '__main__':

    b = [1,2,3,4]
    result = runningsum(b)
    print(result)