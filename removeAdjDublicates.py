class Solution:
  def removeDublicates(self,s):
    stack=[]
    for ch in stack:
      if stack and stack[-1]==ch:
        stack.pop()
      else:
        stack.append(ch)
    return ''.join(stack)
