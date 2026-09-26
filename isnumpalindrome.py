class Solution:
    def isPalindrome(self, x):
        x=str(x)
        for i in range (0,len(x)):
            if x[::-1]==x:
                return True
            else:
                return False


        
