class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        candidate=None
        count=0
        
        for i in nums:
            if count==0:
                candidate=i
                count+=1
            elif i==candidate:
                count+=1
            else:
                count-=1
        print(candidate)
        if candidate!=target:
            return False
        if nums.count(candidate)<=len(nums)//2:
            return False
        return True
                