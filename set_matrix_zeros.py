class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        corr = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    corr.append((i, j))
                    
        for pos in corr:
            for k in range(n): matrix[pos[0]][k] = 0
            for l in range(m): matrix[l][pos[1]] = 0
                        
                    
                    
        