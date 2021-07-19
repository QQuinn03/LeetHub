class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        res = 0
        
        while nums_set:
            i = nums_set.pop()
            n = i+1
            l1=0
            l2=0
            while n in nums_set:
                nums_set.remove(n)
                n=n+1
                l1=l1+1
            n = i-1
            while n in nums_set:
                nums_set.remove(n)
                n = n-1
                l2=l2+1
            print(l1,l2)    
            res = max(res,l2+l1+1)
        return res    