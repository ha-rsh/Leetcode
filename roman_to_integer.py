class Solution:
    def romanToInt(self, s: str) -> int:
        check = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        i = 0
        while i < len(s):
            s1 = check[s[i]]
            if i+1 < len(s):
                s2 = check[s[i+1]]
                if s1 >= s2:
                    ans += s1
                    i += 1
                    
                else: 
                    ans += s2 - s1
                    i += 2
            
            else:
                ans += s1
                i += 1
                
        return ans
    