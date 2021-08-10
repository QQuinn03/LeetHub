class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t ==0 and len(set(nums))==len(nums):
            return False
        bucket = {}
        size = t+1
        nums_size = len(nums)
        
        for i in range(len(nums)):
            key = nums[i]//size
            
            if key in bucket:
                return True
            elif key-1 in bucket and abs(nums[i]-bucket[key-1])<size:
                return True
            elif key+1 in bucket and abs(nums[i]-bucket[key+1])<size:
                
                return True
            
            bucket[key]=nums[i]
            if i>=k:
                del bucket[nums[i-k]//size]
        return False         
            