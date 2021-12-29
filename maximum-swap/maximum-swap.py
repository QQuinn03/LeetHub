class Solution:
    def maximumSwap(self, num: int) -> int:
        arr=list(str(num))
        size=len(arr)
    
        idx=0
        while idx+1<size:
            if arr[idx]<arr[idx+1]:
                break        
            idx+=1
            
        if idx==size-1:
            return num
        
        max_idx = idx+1
        max_val=arr[idx+1]
        
        for i in range(idx+1,size):
            if max_val <=arr[i]:
                max_val=arr[i]
                max_idx=i
        left_idx=idx
        for i in range(idx,-1,-1):
            if arr[i]<max_val:
                left_idx=i
        
        arr[left_idx],arr[max_idx]=arr[max_idx],arr[left_idx]
        return int("".join(arr))
                
        
    