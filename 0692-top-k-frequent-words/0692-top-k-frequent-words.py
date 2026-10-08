class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        heap=[]
        freq={}
       
        for word in words:
            freq[word]=freq.get(word,0)+1
        for word,val in freq.items():
            heapq.heappush(heap,(-val,word))
        ans=[]
        for i in range(k):
            val, word = heapq.heappop(heap)
            ans.append(word)
        return ans

        