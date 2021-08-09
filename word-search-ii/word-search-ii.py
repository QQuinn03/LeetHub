class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root 
        for i in word:
            if i not in cur.children:
               
                new = TrieNode()
                cur.children[i]=new
            cur = cur.children[i]    
        cur.is_word = True
    def search(self,word):
        cur = self.root 
        for i in word:
            if i not in cur.children:
            
                return False
            
            cur = cur.children[i]
         
        return cur.is_word     
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
          
        res =[]
        path = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,node,res,path,i,j)
        return res
    
    def dfs(self,board,node,res,path,i,j):
        if node.is_word:
       
            res.append(path)
            node.is_word = False
           
        if i <0 or i >=len(board) or j<0 or j >=len(board[0]):
            return 
        temp = board[i][j]

        node = node.children.get(temp)
    
        if not node:
          
            return
        board[i][j]="#"
        self.dfs(board,node,res,path+temp,i+1,j)
        self.dfs(board,node,res,path+temp,i-1,j)
        self.dfs(board,node,res,path+temp,i,j+1)
        self.dfs(board,node,res,path+temp,i,j-1)
        board[i][j]=temp
       
        
            
        