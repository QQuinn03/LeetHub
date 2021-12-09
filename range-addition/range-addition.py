class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res=[0 for i in range(length)]
        
        for update in updates:
            start=update[0]
            end=update[1]
            val=update[2]
            
            res[start]+=val
            if end+1<len(res):
                res[end+1]-=val
       
        for i in range(1,len(res)):
            res[i]+=res[i-1]
        return res    
             