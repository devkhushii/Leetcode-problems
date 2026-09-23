class Solution:
    def permutation(self,nums, current, used, result):
        if len(current)==len(nums):
            result.append(current.copy())
            return
        
        for num in nums:
            if num not in used:
                current.append(num)
                used.add(num)
                self.permutation(nums,current,used,result)

                current.pop()
                used.remove(num)

    def permute(self, nums: list[int]) -> list[list[int]]:
        current=[]
        result=[]
        used=set()
        self.permutation(nums, current, used, result)
        return result
        