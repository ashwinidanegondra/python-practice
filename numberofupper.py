class Solution:
  def numberofupper(self,s):
    
    count=0
    for ch in s:
      if ch.isupper():
        count+=1
    return count
