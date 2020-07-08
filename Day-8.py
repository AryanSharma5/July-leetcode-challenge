class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                temp = nums[i]+nums[l]+nums[r]
                if temp==0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif temp<0:
                    l+=1
                else:
                    r-=1
        return list(ans)Day-8.py