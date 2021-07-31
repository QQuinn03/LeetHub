class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag =1
        min_num = -2**31
        max_num = 2**31-1
        if x <0:
            flag = -1
            x= abs(x)
        while x!=0 :
            temp = x%10
            res = res*10+temp
            x = x //10
        
        if flag *res>max_num or flag*res<min_num:
            return 0
        if flag*res<0:
            return max(min_num,flag*res)
        return min(max_num,flag*res)