class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def dfs(exp):
            j = exp.find('}')

            # No braces left
            if j == -1:
                result.add(exp)
                return

            # Find matching opening brace
            i = exp.rfind('{', 0, j)

            before = exp[:i]
            after = exp[j + 1:]

            # Try every option inside the braces
            for option in exp[i + 1:j].split(','):
                dfs(before + option + after)

        result = set()

        dfs(expression)

        return sorted(result)