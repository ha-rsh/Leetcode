import numpy

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        curr_sum = numpy.sum(target)
        target = [-i for i in target]
        heapq.heapify(target)
        while target[0] != -1:
            top = (-1) * heapq.heappop(target)
            curr_sum -= top
            if curr_sum == 1: return True
            if curr_sum == 0 or curr_sum >= top or top % curr_sum == 0: return False
            top %= curr_sum
            curr_sum += top
            heapq.heappush(target, -top if top > 0 else curr_sum )
        return True