class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i =0
        j=0
        k=0
        count = 1
        while count<n:
            val = min(2*res[i],min(3*res[j],5*res[k]))
        
            if val==res[i]*2:
                i+=1
            if val==res[j]*3:
                j+=1
            if val==res[k]*5:
                k+=1
            count+=1
            res.append(val)
        return res[-1]    