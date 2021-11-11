class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        required=0
        visited=[[0 for i in range(col)] for j in range(row)]
        
        for i in range(row):
            for j in range(col):
                if self.helper(board,i,j,required,word,row,col,visited)==True:
                    return True
        return False        
    
    def helper(self,board,i,j,required,word,row,col,visited):
        if required==len(word):
            return True
        if i<0 or j<0 or i>=row or j>=col or board[i][j]!=word[required]:
            return False
        if visited[i][j]==True:
            return False
        visited[i][j]=True
        required+=1
        
        if self.helper(board,i+1,j,required,word,row,col,visited)==True:
            return True
        if self.helper(board,i-1,j,required,word,row,col,visited)==True:
            return True
        if self.helper(board,i,j-1,required,word,row,col,visited)==True:
            return True
        if self.helper(board,i,j+1,required,word,row,col,visited)==True:
            return True
        visited[i][j]=False
                