class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                pos = nums.index(target - nums[i])
                if i == pos:
                    continue
                return [i,pos]
                