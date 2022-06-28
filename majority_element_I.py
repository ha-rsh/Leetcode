class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maximum = -maxsize
        freq = Counter(nums)
        for i, j in freq.items():
            if j > maximum: 
                maximum = j
                ans = i
                    
        return ans