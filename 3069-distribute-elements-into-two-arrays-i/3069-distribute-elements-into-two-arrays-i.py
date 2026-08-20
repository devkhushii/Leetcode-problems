class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums1=[]
        nums2=[]
        nums1.append(nums[0])
        nums2.append(nums[1])
        for i in range(2,n):
            if nums1[-1]>nums2[-1]:
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
        return nums1+nums2
        