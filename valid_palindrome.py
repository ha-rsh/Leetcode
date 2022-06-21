class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if i.isalnum():
                ans += i.lower()
                
        return True if ans == ans[::-1] else False
        
