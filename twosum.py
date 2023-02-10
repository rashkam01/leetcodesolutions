''''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
'''



def twoSum(mylist, target):
    opt = []
    itter = len(mylist)
    #print(itter)
    for i in range(itter-1): 
        tempTarget = mylist[i]+ mylist[i+1]
        if target == tempTarget:
            opt.append(i)
            opt.append(i+1)
    return opt 


if __name__ == '__main__':

    listInpt = [2, 7, 11, 15]
    target = 9
    result = twoSum(listInpt,target)
    print(result)