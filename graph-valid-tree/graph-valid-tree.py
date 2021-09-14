class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        dic = {i:set()for i in range(n)}
        for i,neighbour in edges:
            dic[i].add(neighbour)
            dic[neighbour].add(i)
            
        stack=[0]
        seen=set()
        
        while stack:
            node=stack.pop()
            if node in seen:
                return False
            seen.add(node)
            for neighbour in dic[node]:
                stack.append(neighbour)
                dic[neighbour].remove(node)
        if len(seen)!=n:
            return False
        return True
        