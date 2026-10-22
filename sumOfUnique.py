class Solution:
    def sumOfUnique(self, nums ) :
        sum=0
        for n in nums:
            if nums.count(n)==1:
                sum+=n
        return sum
