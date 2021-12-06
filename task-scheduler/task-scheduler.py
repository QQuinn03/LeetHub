class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr=[0]*26
        for i in tasks:
            arr[ord(i)-ord("A")]+=1
        
        arr.sort()
        max_task=arr.pop()
        max_idle = (max_task-1)*n
        
        while arr and max_idle>=0:
            max_idle=max_idle-min(max_task-1,arr.pop())
        max_idle = max(0,max_idle) 
        return max_idle+len(tasks)
       