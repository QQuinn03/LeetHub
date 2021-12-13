from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course={i:set() for i in range(numCourses)}
        pre={i:set() for i in range(numCourses)}
        
        
        for i in prerequisites:
            course[i[0]].add(i[1])
            pre[i[1]].add(i[0])
        
        que=deque([])
        for i in course:
            if len(course[i])==0:
                que.append(i)
        
        res=[]
        
        while que:
            node=que.popleft()
            res.append(node)
            for nei in pre[node]:
                course[nei].remove(node)
                if len(course[nei])==0:
                    que.append(nei)
        if len(res)!=numCourses:
            return []
        return res            