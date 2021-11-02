from collections import deque
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n=len(colors)
        graph=defaultdict(list)
        indegree=defaultdict(int)
        
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        
        que =deque([])
        dp=[[0]*26 for i in range(n)]
        color_value=[ord(i)-ord("a") for i in colors ]
        for u in range(n):
            if u not in indegree:
                que.append(u)
                dp[u][color_value[u]]=1
              
        visited=0
        while que:
            u = que.pop()
            visited+=1
            for nei in graph[u]:
                for c in range (26):
                    dp[nei][c]=max(dp[nei][c],dp[u][c]+(c==color_value[nei]))
                indegree[nei]-=1
                if indegree[nei]==0:
                    que.append(nei)
                    del indegree[nei]
               
        if visited<n:
            return -1
        return max(max(x)for x in dp)                
                    