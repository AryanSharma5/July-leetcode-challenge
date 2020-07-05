class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = 0
        i = 1
        while s <= n:
            s = i*(i+1)//2
            i += 1
        return i-2