class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        res = []

        for x, y in points:
            distance = x**2 + y**2
            heap.append((-distance, [x,y]))


        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        
        for _, point in heap:
            res.append(point)

        return res

        