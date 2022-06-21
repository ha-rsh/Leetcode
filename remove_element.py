class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                nums.append("_")
                
            else: i += 1                
        count = 0
        for i in range(len(nums)):
            if nums[i] != "_":
                count += 1
                
        return count