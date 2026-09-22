class Solution:
    def printSubsets(self,nums,ans,i,sub):
        
        if i==len(nums):
            sub.append(ans.copy())
            return
        ans.append(nums[i])
        self.printSubsets(nums,ans,i+1,sub)

        ans.pop()
        self.printSubsets(nums,ans,i+1,sub)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        sub=[]
        ans=[]
        self.printSubsets(nums,ans,0,sub)
        return sub

        