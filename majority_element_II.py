class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        freq = Counter(nums)
        for i, j in freq.items():
            if j > len(nums) // 3: ans.append(i)
                    
        return ans