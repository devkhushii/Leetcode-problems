class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)

            elif ch == '*':
                stars.append(i)

            else:
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while stack and stars:
            if stack[-1] < stars[-1]:
                stack.pop()
                stars.pop()
            else:
                return False

        return not stack