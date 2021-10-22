class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for idx,val in enumerate(nums):
            if val not in dic:
                dic[val]=idx
            else:
                if abs(dic[val]-idx)<=k:
                    return True
                dic[val]=idx
        return False        