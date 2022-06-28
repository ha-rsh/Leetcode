import numpy

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums): return False
        l = {}
        for i in range(len(nums)):
            if nums[i] not in l: l[nums[i]] = i
            else:
                if abs(i - l[nums[i]]) <= k: return True
                l[nums[i]] = i
                
        return False