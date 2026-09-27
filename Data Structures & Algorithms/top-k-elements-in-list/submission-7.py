class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        res = []


        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, value in count.items():
            heapq.heappush(heap, (-value, key))

        while k > 0 and heap:
            neg_freq, val = heapq.heappop(heap)
            res.append(val)
            k-=1

        return res
