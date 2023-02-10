import numpy

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = [int(a) for a in str(n)]
        add = sum(x)
        mul = numpy.prod(x)
        result = mul - add 
        return result 

s = Solution()
s.subtractProductAndSum(5)
print(s.subtractProductAndSum)