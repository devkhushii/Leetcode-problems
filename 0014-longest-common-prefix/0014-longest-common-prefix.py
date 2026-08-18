class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if not strs:
            return ""
        shortest=min(strs,key=len)
        for i,ch in enumerate(shortest):
            for s in strs:
                if ch!=s[i]:
                    return shortest[:i]

        return shortest
        