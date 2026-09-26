class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        ans=[]
        part=[]
        nums=[i for i in range(1,n+1)]

        def backtrack(nums,i,k,ans,part):
            
            if len(part)==k:
                ans.append(part[:])
                return 
            if i==len(nums):
                return 
            part.append(nums[i])
            backtrack(nums,i+1,k,ans,part)
            part.pop()

            backtrack(nums, i + 1, k, ans, part)
        
        backtrack(nums,0,k,ans,part)
        return ans

            
            

            
        