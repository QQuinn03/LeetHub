class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res=[]
        for i in range(len(arr)):
            if i==0 and arr[i]!=1:
                for j in range(1,arr[i]):
                    res.append(j)
            
            if i >=0 and arr[i]-arr[i-1]>1:
                for j in range(arr[i-1]+1,arr[i]):
                    res.append(j)
        if len(res)>=k:
            return res[k-1]
        if len(res)==0:
            return arr[-1]+k
        if 0<len(res)<k:
            return k-len(res)+arr[-1]