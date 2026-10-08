class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        result=[]
        for i in range (len(tokens)):
            if tokens[i]=='+':
                result.append(result.pop()+result.pop())
            elif tokens[i]=='-':
                a,b=result.pop(),result.pop()
                result.append(b-a)
            elif tokens[i]=='*':
                result.append(result.pop()*result.pop())
            elif tokens[i]=='/':
                a,b=result.pop(),result.pop()
                result.append(int(b/a))
            else:
                result.append(int(tokens[i]))
        return result[-1]
