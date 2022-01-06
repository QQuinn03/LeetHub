class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph=defaultdict(set)
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        
        total=n
        
        leaves=[]
        for i in graph:
            if len(graph[i])==1:
                leaves.append(i)
        
        while total>2:
            total-=len(leaves)
            next_level=[]
            
            for leave in leaves:
                for nei in graph[leave]:
                    graph[nei].remove(leave)
                    if len(graph[nei])==1:
                        next_level.append(nei)
            leaves=next_level
        return leaves    
            
               
                        
                        
                        
                        