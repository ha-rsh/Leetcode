class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        strs.sort()
        end = min(len(strs[0]), len(strs[len(strs) - 1]))
        i = 0
        while i < end and strs[0][i] == strs[len(strs) - 1][i]:
            i += 1
        
        return strs[0][:i]