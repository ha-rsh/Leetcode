import numpy

class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = []
        while num != 0:
            num_list.append(num % 10)
            num //= 10
            
        num_list.sort()
        heapq.heapify(num_list)
        new_nums = []
        for i in range(len(num_list) // 2):
            new_nums.append(heapq.heappop(num_list))
            
        for i in range(len(new_nums)):
            new_nums[i] = (new_nums[i] * 10) + heapq.heappop(num_list)
            
        ans = numpy.sum(new_nums)
        return ans