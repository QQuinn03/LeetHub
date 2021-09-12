class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        start = 0
        end = 0
        max_cur = 0
        
        while end <len(nums)-1:
            step+=1
            for i in range(start,end+1):
                if i +nums[i]>=len(nums)-1:
                    print(i+nums[i])
                    return step
                max_cur = max(max_cur,i+nums[i])
            start=end+1
            end = max_cur
            print(end)
        return step    