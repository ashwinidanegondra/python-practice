class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        new=""
        for ch in s:
            if ch.isalnum():
                new+=ch
                

        if new[::-1]==new:
            return True
        else:
            return False
        
