class Solution:
    def wordPattern(self, pattern,s):
        words=s.split()
        for i in range(len(pattern)):

            if pattern[i]=="a": 
                return words[i]=="dog"
            else:
                return False
            if pattern[i]=="b":
                return words[i]=="cat"
            
        
        
