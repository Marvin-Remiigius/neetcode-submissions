class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums)
        
        freqList = []

        for key, val in freqDict.items():
            freqList.append([key,val])

        freqList = sorted(freqList, key = lambda item : item[1])
        final = []
        for _ in range(k):
            final.append(freqList.pop()[0])
        return final