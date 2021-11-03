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
        for i in dic:
            print(i,dic[i])
            heapq.heappush(que,(-dic[i],i))
        res=[]    
        while k>0:
            fre,val = heapq.heappop(que)
           
            res.append(val)
            k-=1
        return res    
            