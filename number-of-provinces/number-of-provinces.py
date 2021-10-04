class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        res=0
        
        for i in range(row):
            if isConnected[i][i]==1:
                res+=1
                self.dfs(i,row,isConnected)
        return res
    
    def dfs(self,cur,row,isConnected):
        for i in range(row):
            if isConnected[cur][i]==1:
                isConnected[cur][i] = isConnected[i][cur]=0
                self.dfs(i,row,isConnected)
                
        
            
        
        