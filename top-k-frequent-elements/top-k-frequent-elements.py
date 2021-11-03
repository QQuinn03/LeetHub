import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        
        que=[]
        for key,val in dic.items():
            if len(que)==k:
                heapq.heappushpop(que,(val,key))
            else:
                heapq.heappush(que,(val,key))
        res=[]
        for i in que:
            res.append(i[1])
        return res    
        
