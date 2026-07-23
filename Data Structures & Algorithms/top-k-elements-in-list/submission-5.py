class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        freqDict = Counter(nums)

        for key,val in freqDict.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for h in heap:
            res.append(h[1])

        return res

        