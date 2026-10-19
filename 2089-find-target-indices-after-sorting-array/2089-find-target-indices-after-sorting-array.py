class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans=[]
        left=0
        right=len(nums)-1
        # while left<right:
        #     mid=(left+right)//2

        #     if nums[mid]==target:
        #         ans.append(mid)
        #     elif nums[mid]>target:
        #         right=mid
        #     else:
        #         left=mid+1
        # return ans

        for i in range(right+1):
            if nums[i]==target:
                ans.append(i)
        return ans
