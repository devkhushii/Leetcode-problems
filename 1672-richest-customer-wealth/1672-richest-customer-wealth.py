class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row=len(accounts)
        col=len(accounts[0])
        max_wealth=0
        for i in range(row):
            max_wealth=max(max_wealth,sum(accounts[i]))
        return max_wealth
        