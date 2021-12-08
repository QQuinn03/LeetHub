class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res=[]
        products.sort()
        for i in range(len(searchWord)):
            prefix=searchWord[:i+1]
            arr=[]
            count=0
        
            for word in products:
                suggest=word[:i+1]
             
                if suggest==prefix:
                    arr.append(word)
                    count+=1
                if count==3:
                    
                    break
            res.append(arr)    
        return res            
                
        
        