class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        x,y=len(matrix),len(matrix[0])
        dp=[[0 for i in range(y+1)] for j in range(x+1)]
        for i in range(x-1,-1,-1):
            for j in range(y-1,-1,-1):
                if matrix[i][j]!='1': continue
                dp[i][j]=max(dp[i][j], 1+min([dp[i+1][j],dp[i][j+1],dp[i+1][j+1]]))
        
        return max(sum(dp,[]))**2
        