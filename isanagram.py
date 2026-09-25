class Solution:
    def isAnagram(self, s,t):
            if len(t)!=len(s):
                return False
            return sorted(s)==sorted(t)
        
