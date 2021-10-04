from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(dict)
        
        for i in range(len(equations)):
            x=equations[i][0]
            y=equations[i][1]
            val = values[i]
            graph[x][y]=val
            graph[y][x]=1/val
        res=[]
        for i in queries:
            start=i[0]
            end =i[1]
            if start not in graph or end not in graph:
                res.append(-1.0)
                continue
            else:
                res.append(self.bfs(start,end,graph))
        return res
    
    def bfs(self,start,end,graph):
        que = deque([(start,1.0)])
        seen=set()
        seen.add(start)
        res=1.0
        while que:
            node,val = que.popleft()
            
            if node==end:
                return val
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    que.append((nei,val*graph[node][nei]))
        return -1            
                    
                
        
        
            