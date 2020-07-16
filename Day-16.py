class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = -n if n < 0 else n
        y = 1
        while m:
            if m & 1:
                y *= x
            x *= x
            m >>= 1
        return y if n >= 0 else 1/y