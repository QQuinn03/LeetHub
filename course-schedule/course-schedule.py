from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course={i:set() for i in range(numCourses)}
        todo = {i:set() for i in range(numCourses)}
        
        for i in prerequisites:
            class_=i[0]
            pre=i[1]
            course[class_].add(pre)
            todo[pre].add(class_)
        que=deque([])
        for i in course:
            if len(course[i])==0:
                que.append(i)
        
        visited=[]
        
        while que:
            node = que.popleft()
            visited.append(node)
            for nei in todo[node]:
                course[nei].remove(node)
                if len(course[nei])==0:
                    que.append(nei)
                    
        if len(visited)!=numCourses:
            return False
        return True
                    
                
                
                
                
        
        
            
        
            
        