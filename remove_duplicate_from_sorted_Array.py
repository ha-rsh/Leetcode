class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i - 1] == nums[i] and nums[i] != "_":
                nums.pop(i)
                nums.append("_")
                
            else: i += 1
                
        count = 0
        for i in nums:
            if i != "_": count += 1
        
        return count