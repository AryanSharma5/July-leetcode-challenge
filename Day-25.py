class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while l<h:
            while l<h and nums[l] == nums[l+1]:
                l += 1
            while h>l and nums[h] == nums[h-1]:
                h -= 1
            if l == h:
                return nums[l]
            mid = (h+l)//2
            if nums[mid]<nums[h]:
                h = mid
            else:
                l = mid+1
        return nums[l]