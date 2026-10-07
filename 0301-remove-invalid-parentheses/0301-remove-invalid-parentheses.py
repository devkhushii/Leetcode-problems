from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}

        while queue:
            level_size = len(queue)
            answer = []

            for _ in range(level_size):
                current = queue.popleft()

                if is_valid(current):
                    answer.append(current)

                # If we found valid strings at this level,
                # don't generate strings with more removals.
                if answer:
                    continue

                for i in range(len(current)):
                    if current[i] not in '()':
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)

            if answer:
                return answer

        return [""]
        