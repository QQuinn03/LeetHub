class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        for idx,char in enumerate(order):
            dic[char]=idx
            
        for i in range(1,len(words)):
            flag=0
            for j in range(min(len(words[i]),len(words[i-1]))):
                if dic[words[i-1][j]]>dic[words[i][j]]:
                    return False
                if dic[words[i-1][j]]<dic[words[i][j]]:
                    flag=1
                    break
            if flag==0 and len(words[i-1])>len(words[i]):
                return False
        return True     
                
       
        
                
                    
       
        
        
      
        