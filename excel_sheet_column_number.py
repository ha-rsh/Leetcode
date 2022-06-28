class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = dict(zip(ascii_uppercase, range(1, 27)))
        ans = 0
        columnTitle = columnTitle[::-1]
        for i in range(len(columnTitle)):
            ans += (pow(26,i) * val[columnTitle[i]])
                    
        return ans