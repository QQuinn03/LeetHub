from collections import deque,defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for i in tickets:
            from_ = i[0]
            to_ = i[1]
            graph[from_].append(to_)
        
        for from_,to_ in graph.items():
            to_.sort(reverse=True)
            
        que = deque(["JFK"])
        
        res=[]
        while que:
            from_ = que[-1]
            if len(graph[from_])>0:
                que.append(graph[from_].pop())
            else:
                res.append(que.pop())
        return res[::-1]        
                
            
            