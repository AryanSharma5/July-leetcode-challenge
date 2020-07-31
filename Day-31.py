class Solution:
    def climbStairs(self, n: int) -> int:
        def Helper(i, n, memo):
            if i>n:
                return 0
            if i==n:
                return 1
            if memo[i]>0:
                return memo[i]
            else:
                memo[i] =  Helper(i+1, n, memo) + Helper(i+2, n, memo)
                return memo[i]
            
        memo = [0]*(n)
        return Helper(0, n, memo)