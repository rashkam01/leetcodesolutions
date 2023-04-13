class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_count = bin(n).count('1')
        return binary_count