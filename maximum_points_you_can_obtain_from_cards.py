import numpy

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        total = numpy.sum(cardPoints)
        if len(cardPoints) == k: return total
        curr_sum = 0
        for i in range(len(cardPoints)-k-1):
            curr_sum += cardPoints[i]
            
        for i in range(len(cardPoints)-k-1, len(cardPoints)):
            curr_sum += cardPoints[i]
            ans = max(ans, total - curr_sum)
            curr_sum -= cardPoints[i-(len(cardPoints) - k - 1)]
            
        return ans
            
                