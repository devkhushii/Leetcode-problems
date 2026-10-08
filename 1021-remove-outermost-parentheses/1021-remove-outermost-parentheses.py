class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ans=""
        o=0
        c=0
        for i in range(len(s)):
            stack.append(s[i])
            if s[i]=='(':
                
                o+=1
            else:
             
                c+=1
            if c==o:
                stack=stack[1:len(stack)-1]
                ans+="".join(stack)
                while stack:
                    stack.pop()
                c=0
                o=0
        return ans