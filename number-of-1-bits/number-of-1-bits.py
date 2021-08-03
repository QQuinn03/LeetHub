class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        bit = 1
        while n:
            if 1&n:
                res+=1
            n>>=1
        return res    