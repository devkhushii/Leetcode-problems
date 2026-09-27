# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         stack=[]
        
#         i=0
#         while i<len(s):
#             if s[i]==')':
#                 word=""
#                 while stack and stack[-1]!='(':
#                     word+=stack[-1]
#                     stack.pop()
#                 if stack:
#                     stack.pop()
#                 for ch in word:
#                     stack.append(ch)
#             if s[i]==')':
#                 i+=1
#                 continue
#             stack.append(s[i])
#             i+=1

#         return "".join(stack)

    
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]

        for ch in s:
            if ch == '(':
                stack.append("")
            elif ch == ')':
                temp = stack.pop()
                stack[-1] += temp[::-1]
            else:
                stack[-1] += ch

        return stack[0]