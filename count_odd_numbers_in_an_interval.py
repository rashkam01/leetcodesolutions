class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #check if odd number or even 
        if(low % 2 !=0 and high % 2 !=0): # only if both are odd 
            result = 1 + (high + 1 - low) // 2 # //2 is floor division rounds to nearest whole number 
        else:  #if either is even 
            result = (high + 1 - low) // 2  
        return result 



""""
Details
Runtime: 48 ms, faster than 31.19% of Python3 online submissions for Count Odd Numbers in an Interval Range.
Memory Usage: 13.9 MB, less than 59.15% of Python3 online submissions for Count Odd Numbers in an Interval Range.
"""