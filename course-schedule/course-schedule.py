from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course={i:set() for i in range(numCourses)}
        todo={i:set() for i in range(numCourses)}
        
        for i in prerequisites:
            course[i[0]].add(i[1])
            todo[i[1]].add(i[0])
        que = deque([])
        for i in course:
            if len(course[i])==0:
                que.append(i)
        seen=set()
        while que:
            node =que.popleft()
           
            seen.add(node)
            for nei in todo[node]:
                course[nei].remove(node)
                if len(course[nei])==0:
                    que.append(nei)
        if len(seen)!=numCourses:
            return False
        return True
            
        
       
    
            