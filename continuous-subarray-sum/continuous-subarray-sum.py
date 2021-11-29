class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic={0:-1}
        total=0
        
        for i in range(len(nums)):
            total+=nums[i]
            if total%k not in dic:
                dic[total%k]=i
            else:
                if i-dic[total%k]>=2:
                    return True
        return False    