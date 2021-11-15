class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        dp=[[0 for i in range(col)] for j in range(row)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        ans=0
        for i in range(row):
            for j in range(col):
                ans=max(ans,self.dfs(matrix,i,j,dp,directions))
        return ans
    
    def dfs(self,matrix,i,j,dp,directions):
        if dp[i][j]!=0:
            return dp[i][j]
        longest=0
        for x in directions:
            new_i= i+x[0]
            new_j = j+x[1]
            if 0<=new_i<len(matrix) and 0<=new_j<len(matrix[0]) and matrix[new_i][new_j]>matrix[i][j]:
                longest=max(longest,self.dfs(matrix,new_i,new_j,dp,directions))
        dp[i][j]=1+longest
        return dp[i][j]
            