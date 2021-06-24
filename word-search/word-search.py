class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        required = 0
        row = len(board)
        col = len(board[0])
        visited = [[0 for i in range(col)]for j in range(row)]
        
        for i in range(row):
            for j in range(col):
                if self.helper(i,j,row,col,required,word,board,visited)==True:
                    return True
        return False        
    
    def helper(self,i,j,row,col,required,word,board,visited):
        if required == len(word):
            return True
        if i <0 or i >=row or j <0 or j >=col or board[i][j]!=word[required]:
            return False
        
        if visited[i][j]==True:
            return False
        
        required+=1
        visited[i][j]=True
        existed = self.helper(i+1,j,row,col,required,word,board,visited)
        if existed ==True:
            return True
        
        existed = self.helper(i-1,j,row,col,required,word,board,visited)
        if existed ==True:
            return True
        existed = self.helper(i,j+1,row,col,required,word,board,visited)
        if existed ==True:
            return True
        existed = self.helper(i,j-1,row,col,required,word,board,visited)
        if existed ==True:
            return True
        
        visited[i][j]=False
        
            
        
        
