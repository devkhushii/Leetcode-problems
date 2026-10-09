class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq={}
        for ch in tasks:
            freq[ch]=freq.get(ch,0)+1
        heap=[]
        for key,val in freq.items():
            heapq.heappush(heap,(-val,key))
        queue=deque()
        time=0

        while heap or queue:

            time+=1
            if heap:
                count,task=heapq.heappop(heap)
                count+=1
                if count<0:
                    queue.append((count,task,time+n))
            if queue and queue[0][2]==time:
                count,task,Atime=queue.popleft()
                heapq.heappush(heap,(count,task))
        return time
        
            

