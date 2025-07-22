class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        count = 0
        for x,y in points:
            value = (x*x) + (y*y)
            heapq.heappush(heap, (-value,(x,y)))
            count+=1
            if count > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            value,(x,y) = heapq.heappop(heap)
            res.append([x,y])
        return res