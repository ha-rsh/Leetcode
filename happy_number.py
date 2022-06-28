import numpy

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            curr_sum = 0
            while n != 0:
                curr_sum += (n % 10) * (n % 10)
                n //= 10
                
            if curr_sum in s: return False
            s.add(curr_sum)
            n = curr_sum
            
        return True
                
            