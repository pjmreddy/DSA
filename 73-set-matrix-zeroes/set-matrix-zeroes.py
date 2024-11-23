class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        r,c=len(matrix), len(matrix[0])
        matcopy=[row[:] for row in matrix]

        for row in range(r):
            for col in range(c):
                if matrix[row][col]==0:
                    for i in range(c):
                        matcopy[row][i]=0
                    for j in range(r):
                        matcopy[j][col]=0
        
        for row in range(r):
            for col in range(c):
                matrix[row][col]=matcopy[row][col]
