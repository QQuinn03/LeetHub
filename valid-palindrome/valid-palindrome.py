class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        
        while left<right:
            while left<right and not s[left].isalpha() and not s[left].isdigit():
                left+=1
            while left<right and not s[right].isalpha() and not s[right].isdigit():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
            
        return True    