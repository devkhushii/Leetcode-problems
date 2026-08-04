class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=float("inf")
        maxi=float("-inf")
        ans=[]
        for num in nums:
            if maxi<num:
                maxi=max(maxi,num)
            if mini>num:
                mini=min(mini,num)
        
        for i in range(mini,maxi+1):
            if i not in nums:
                ans.append(i)
        
        return ans

        