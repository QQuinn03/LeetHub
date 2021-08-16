class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_int = 2**31-1
        min_int = -2**31
        
        if dividend ==0:
            return 0
        flag = 1
        if dividend <0<divisor or divisor <0<dividend:
            flag = -1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
 
        res = 0
        
        while dividend >=divisor:
            temp = divisor 
            power=1
            while dividend >=temp:
                dividend -=temp
                temp*=2
               
                res+=power
                power*=2
                print(dividend,temp,res,power)
        if flag==-1:
            return max(min_int,res*flag)
        else:
            return min(max_int,res)