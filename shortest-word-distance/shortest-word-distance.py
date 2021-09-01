class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = -1
        w2 = -1
        res = len(wordsDict)
        for idx,val in enumerate(wordsDict):
            if word1==val:
                w1=idx
            elif word2==val:
                w2=idx
            if w1!=-1 and w2!=-1:    
                res = min(res,abs(w1-w2))    
              
                
        return res      