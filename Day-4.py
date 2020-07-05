class Solution:
    ugly = sorted([2**i*3**j*5**k for i in range(32) for j in range(32) for k in range(32)])
    def nthUglyNumber(self, n: int) -> int:    
        return self.ugly[n-1]