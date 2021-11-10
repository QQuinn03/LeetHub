class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        temp = 0
        
        for i in range(len(nums)):
            temp +=nums[i]
            if k!=0:
                temp = temp %k
            if temp in dic:
                if i-dic[temp]>1:
                    return True
            else:
                dic[temp]=i
        return False         

        
        
        