class Solution:
    def permutation(self,nums, current, used, result):
        if len(current)==len(nums):
            result.append(current.copy())
            return
        
        for i in range(len(nums)):
            if  not used[i]:
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                current.append(nums[i])
                used[i]=True
                self.permutation(nums,current,used,result)

                current.pop()
                used[i]=False

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        current=[]
        result=[]
        used=[False] * len(nums)
        self.permutation(nums, current, used, result)
        return result
        
        