class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            curr_sum = 0
            while num != 0:
                curr_sum += num % 10
                num = num // 10
                
            if curr_sum // 10 == 0: return curr_sum
            num = curr_sum
            
        