class Solution:
    def addDigits(self, num: int) -> int:
        if num <10:
            return num
        res=0
        while num >=0:
            res+=num%10
            num//=10
            print(num,res)
            if res>=10 and num ==0:
                num=res
                res=0
            elif res<10 and num==0:
                return res