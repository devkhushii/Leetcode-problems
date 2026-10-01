class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for ch in s:
            if ch==')' or ch=='}' or ch==']':
                if ch==')' and stack and stack[-1]!='(':
                    return False
                elif ch==']' and stack and stack[-1]!='[':
                    return False
                elif ch=='}' and stack and stack[-1]!='{':
                    return False
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(ch)
        if stack:
            return False
        return True
        