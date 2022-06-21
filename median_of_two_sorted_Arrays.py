class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        if len(nums1) % 2:
            mid = (len(nums1) - 1) // 2
            return nums1[mid]
        
        else:
            val1 = len(nums1) // 2
            ans = (nums1[val1] + nums1[val1 - 1]) / 2
            return ans