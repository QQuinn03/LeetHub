class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high=sum(weights)
        day=1
       
        while low<high:
            day=1
            mid=low+(high-low)//2
            total=0
            for weight in weights:
                total+=weight
                if total>mid:
                    day+=1
                    total=weight
            if day>days:
                low=mid+1
            else:
                high=mid
        return low       
                
                