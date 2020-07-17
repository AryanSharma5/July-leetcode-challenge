from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # O(nlogn)
        
        # dict = {}
        # for i in nums:
        #     if i not in dict:
        #         dict[i]=1
        #     else:
        #         dict[i]+=1
        # sorted_keys = sorted(dict, key = lambda x: dict[x])[::-1]
        # ans = []
        # ans.extend(sorted_keys[:k])
        # return ans
        
        # O(n)
        
        bucket = [[] for i in range(len(nums) + 1)]
        for item, freq in Counter(nums).items():
            bucket[freq].append(item)
        ans = [item for sublist in bucket for item in sublist][::-1][:k]
        return ans