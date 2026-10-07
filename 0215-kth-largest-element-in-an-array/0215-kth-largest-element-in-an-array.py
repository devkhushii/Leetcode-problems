class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        ans=heapq.nlargest(k, nums)
        return ans[-1]
        