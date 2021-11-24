class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum =0
        
        for i in w:
            prefix_sum +=i
            self.prefix_sums.append(prefix_sum)
            
        self.total_sum = prefix_sum      
            
        

    def pickIndex(self) -> int:
        target = self.total_sum*random.random()
        low = 0
        high = len(self.prefix_sums)-1
        
        while low<=high:
            mid = (low+high)//2
            if target<self.prefix_sums[mid]:
                high = mid-1
            else:
                low = mid+1
        return low         
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()