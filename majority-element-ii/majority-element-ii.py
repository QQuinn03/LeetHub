class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:



        
            # 1st pass
            count1, count2, candidate1, candidate2 = 0, 0, None, None
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
                    count1 -= 1
                    count2 -= 1

            # 2nd pass
            result = []
            for c in [candidate1, candidate2]:
                if nums.count(c) > len(nums)//3:
                    result.append(c)

            return result
        # size = len(nums)//3
        # candidate1=None
        # candidate2 =None
        # count1=0
        # count2=0
        # res=[]
        # for n in nums:
        #     if count1==0:
        #         candidate1=n
        #         count1+=1
        #     elif count2==0:
        #         candidate2=n
        #         count2+=1
        #     elif candidate1==n:
        #         count1+=1
        #     elif candidate2==n:
        #         count2+=1
        #     else:
        #         count1-=1
        #         count2-=1
        # print(candidate1,candidate2)
        # for n in [candidate1,candidate2]:
        #     if nums.count(n)>size:
        #         res.append(n)
        # return res       