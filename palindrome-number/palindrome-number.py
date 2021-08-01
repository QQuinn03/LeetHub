class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp = x
        res = 0
        while temp!=0:
            reminder = temp%10
            res = res*10+reminder
            temp = temp//10
        return res ==x    