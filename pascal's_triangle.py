class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        n = numRows
        if n == 1: 
            ans.append([1])

        elif n == 2:
            ans.append([1])
            ans.append([1,1])
            
        else:
            ans.append([1])
            ans.append([1,1])
            for i in range(2, n):
                temp = ans[-1]
                val = []
                val.append(temp[0])
                for j in range(1, len(temp)):
                    val.append(temp[j-1]+temp[j])
                    
                val.append(1)
                ans.append(val)
                
        return ans
                    
        