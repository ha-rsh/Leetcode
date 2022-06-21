class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] == 10:            
            digits[-1] = 0
            carry = 1
            for i in range(len(digits) - 2, -1, -1):
                digits[i] += carry
                if digits[i] == 10:
                    digits[i] = 0
                    carry = 1
                else: carry = 0

            if carry: digits.insert(0,1)
        return digits