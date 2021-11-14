class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        total_node = n
        if total_node==1:
            return [0]
        
        graph={i:set()for i in range(n)}
        for node in edges:
            graph[node[0]].add(node[1])
            graph[node[1]].add(node[0])
            
        leaves=deque([])
        next_level=deque([])
        for i in graph:
            if len(graph[i])==1:
                leaves.append(i)
           
        while total_node>2:
            
            
            next_level=deque([])
            total_node-=len(leaves)
            for leave in leaves:
                nei=graph[leave].pop()
               
                graph[nei].remove(leave)
                if len(graph[nei])==1:
                    next_level.append(nei)
            leaves=next_level            
        return leaves               
                        
                        
                        
                        