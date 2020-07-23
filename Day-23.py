class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        Xor = 0
        for num in nums:
            Xor ^= num
        lowBit = Xor & (-Xor)
        for num in nums:
            if num & lowBit:
                res[0] ^= num
            else:
                res[1] ^= num
        return res