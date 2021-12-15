class Solution:
    def minSwaps(self, data: List[int]) -> int:
        left=0
        right=0
        cur_ones=0
        sum_ones = sum(data)
        max_ones=0
        while right<len(data):
            cur_ones+=data[right]
            right+=1
            if right-left>sum_ones:
                cur_ones-=data[left]
                left+=1
            max_ones=max(max_ones,cur_ones)
        return sum_ones-max_ones    
                

        
            