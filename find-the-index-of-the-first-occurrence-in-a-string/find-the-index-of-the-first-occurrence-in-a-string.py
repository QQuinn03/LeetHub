class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len1 = len(haystack)
        len2= len(needle)
        
        for i in range(len1-len2+1):
            print(haystack[i:len2+i])
            if haystack[i:len2+i]==needle:
                return i
        return -1    