from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        todo = {i:set() for i in range(numCourses)}
        pre = {i:set() for i in range(numCourses)}
        
        for i in prerequisites:
            take,pre_r = i[0],i[1]
            todo[take].add(pre_r)
            pre[pre_r].add(take)
        
        que = deque([])
        for i in todo:
            if len(todo[i])==0:
                que.append(i)
        res = []
        while que:
            course = que.popleft()
            res.append(course)
            for nei in pre[course]:
                todo[nei].remove(course)
                if len(todo[nei])==0:
                    que.append(nei)
        if len(res)==numCourses:
            return True
        return False
            