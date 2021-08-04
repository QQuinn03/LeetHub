class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count =start = 0
        k %=n
        
        while count<n:
            cur,pre = start,nums[start]
            while True:
                nxt_idx = (cur+k)%n
                nums[nxt_idx],pre = pre,nums[nxt_idx]
                cur = nxt_idx
                count+=1
                
                if start==cur:
                    print(start,cur)
                    break
            start+=1
  
        