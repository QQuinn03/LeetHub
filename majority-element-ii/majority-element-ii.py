class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1=None
        candidate2=None
        count1,count2=0,0
        size=len(nums)//3
        for n in nums:

            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1   
            else:
                count1 -=1
                count2 -=1
        print(candidate1,candidate2)         
        res=[]
        for i in [candidate1,candidate2]:
            if nums.count(i)>size and i not in res:
                
                res.append(i)
        return res          
                
            