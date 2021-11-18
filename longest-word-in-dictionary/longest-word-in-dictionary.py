class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        res=""
        seen=set()
        seen.add("")
        
        for word in words:
            for i in range(len(word)):
                if word[:-1] in seen:
                  
                    if len(res)<len(word):
                     
                        res=word
                        
                    seen.add(word)
           
        return res         
        
        