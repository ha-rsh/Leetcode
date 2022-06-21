class Solution:
    def check(self, n, qb):
        if n <= 3: return n
        if qb[n] > 0: return qb[n]
        ans = Solution.check(self, n-1, qb) + Solution.check(self, n-2, qb)
        qb[n] = ans
        return ans
        
    def climbStairs(self, n: int) -> int:
        qb = [0] * (n+1)
        return Solution.check(self, n, qb)
