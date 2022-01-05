from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses ={i:set() for i in range(numCourses)}
        todo={i:set() for i in range(numCourses)}
        
        for i in prerequisites:
            course,pre=i[0],i[1]
            courses[course].add(pre)
            todo[pre].add(course)
        
        que=deque([])
        for i in courses:
            if len(courses[i])==0:
                que.append(i)
        
        seen=set()
        while que:
            node=que.popleft()
            if node not in seen:
                seen.add(node)
            else:
                return False
            for nei in todo[node]:
                courses[nei].remove(node)
                if len(courses[nei])==0:
                    que.append(nei)
        if len(seen)== numCourses:
            return True
        return False
                
        
        
   
            
        
       
    
            