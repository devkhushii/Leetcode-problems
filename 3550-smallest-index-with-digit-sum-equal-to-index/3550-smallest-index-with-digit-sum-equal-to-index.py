class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            num=nums[i]
            s=0
            while num!=0:
                rem=num%10
                s+=rem
                num//=10
            if s==i:
                return i
        return -1
        