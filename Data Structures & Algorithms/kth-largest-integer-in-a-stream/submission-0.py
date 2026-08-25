class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k 
        heapq.heapify(self.minHeap) #use heapify to turn array into min heap
        while len(self.minHeap) > k: #always check heap is same as k
            heapq.heappop(self.minHeap) #pops smallest element from min heap
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #push val onto min heap
        if len(self.minHeap) > self.k: # check if size of heap is equal to k
            heapq.heappop(self.minHeap) #pop element that is not needed

        return self.minHeap[0] # return minimum element
        
