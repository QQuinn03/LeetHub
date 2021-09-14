class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        dic = {}
        def paint(n,color):
            if (n,color) in dic:
                return dic[(n,color)]
            total = costs[n][color]
         
            if n ==len(costs)-1:
                pass
            
            elif color == 0:
                
                total+=min(paint(n+1,1),paint(n+1,2))
                
            elif color ==1:
                total+=min(paint(n+1,0),paint(n+1,2))
                
            else:
                total+=min(paint(n+1,0),paint(n+1,1))
            dic[(n,color)]=total    
            return total
        
        if costs == []:
            return 0
     
        return min(paint(0,0), paint(0,1), paint(0,2))
             
        