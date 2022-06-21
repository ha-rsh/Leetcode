from collections import Counter
from string import ascii_lowercase

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s = list(s)
        freq = Counter(s)
        check = dict(zip(ascii_lowercase, range(1, 27)))
        check = check.fromkeys(check, False)
        ans = ""
        for i in range(len(s)):
            freq[s[i]] -= 1
            if check[s[i]] == False:
                while len(ans) > 0 and ord(ans[-1]) > ord(s[i]) and freq[ans[-1]] > 0:
                    check[ans[-1]] = False
                    ans = ans[:-1]
                    
                ans += s[i]
                check[s[i]] = True
                
        return ans       