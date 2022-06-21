from sys import maxsize

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maximum = -maxsize
        for i in range(len(nums)):
            currsum += nums[i]
            maximum = max(currsum, maximum)
            if currsum < 0:
                currsum = 0
                
        return maximum