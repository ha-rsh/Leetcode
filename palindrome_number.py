class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        if (x < 0) or (x != 0 and x % 10 == 0): return False
        while x > ans:
            ans = ans * 10 + x % 10
            print(ans)
            x = x // 10
            
        return x == ans or x == ans // 10 