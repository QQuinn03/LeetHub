from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        todo = {i:set()for i in range(numCourses)}
        pre= {i:set()for i in range(numCourses)}
        
        for i in prerequisites:
            course=i[0]
            course_pre=i[1]
            todo[course].add(course_pre)
            pre[course_pre].add(course)
            
        que= deque([])
        for i in todo:
            if len(todo[i])==0:
                que.append(i)
        visited=set()
        
        while que:
            node = que.popleft()
            visited.add(node)
            for neighbor in pre[node]:
                todo[neighbor].remove(node)
                if len(todo[neighbor])==0:
                    que.append(neighbor)
        if len(visited)==numCourses:
            return True
        return False
            