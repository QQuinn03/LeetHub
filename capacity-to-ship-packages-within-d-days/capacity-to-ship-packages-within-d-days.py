class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        res=0
        
        while low<high:
            mid=low+(high-low)//2
            total=0
            day=1
            
            for weight in weights:
                total+=weight
                if total>mid:
                    total=weight
                    day+=1
                    
            if day>days:
                low=mid+1
            else:
                high=mid
        return low        
                    
                    
                
            
        