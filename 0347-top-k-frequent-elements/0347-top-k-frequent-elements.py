class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap=[]
        freq={}
     
        for num in nums:
            freq[num]=freq.get(num,0)+1

        for key,val in freq.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        for count, num in heap:
            ans.append(num)

        return ans