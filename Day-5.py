class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x^y
        ans = bin(temp)[2:].count('1')
        return ans