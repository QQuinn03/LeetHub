class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic={0:-1}
        
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            total=total%k
            if total not in dic:
                dic[total]=i
            else:
                if i-dic[total]>=2:
                    return True
        return False      