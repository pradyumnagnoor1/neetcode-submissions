class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        res = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            minHeap.append([distance, (x,y)])

        heapq.heapify(minHeap)

        while k > 0:
            res.append(minHeap[0][1])
            k -= 1
            heapq.heappop(minHeap)

        return res



        