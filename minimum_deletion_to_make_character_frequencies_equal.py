class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        check = []
        op = 0
        for i, j in freq.items(): check.append(j)
        if len(check) == len(set(check)): return op
        check.sort(reverse=True)
        cf = check[0]
        ans = 0
        for i in check:
            if i > cf:
                if cf > 0: ans += (i - cf)
                else: ans += i
                        
            cf = min(cf-1, i-1)
            
        return ans