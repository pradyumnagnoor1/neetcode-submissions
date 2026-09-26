class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)


        while len(stones) >= 2:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, -(y-x))

            else:
                continue


        return -stones[0] if stones else 0
        