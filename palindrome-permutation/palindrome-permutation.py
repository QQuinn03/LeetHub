class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        count = 0
        for key,val in dic.items():
            if val%2==1:
                count+=1
            if count>1:
                return False
        return True    
            
