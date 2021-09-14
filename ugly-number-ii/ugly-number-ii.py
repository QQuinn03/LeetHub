class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[1]
        i=0
        j=0
        k=0
        count =1
        while count<n:
            val = min(res[i]*2,min(res[j]*3,res[k]*5))
            if val==res[i]*2:
                i+=1
            if val ==res[j]*3:
                j+=1
            if val==res[k]*5:
                k+=1
            res.append(val)
            count+=1
        return res [-1]