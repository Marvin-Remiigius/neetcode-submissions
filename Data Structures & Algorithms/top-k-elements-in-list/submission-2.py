class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        my_map = Counter(nums)
        final = []
        my_hash = list(my_map.items())
        my_hash.sort(key=lambda x: x[1])
        for i in my_hash[::-1]:
            if k!= 0 :
                final.append(i[0])
                k-=1
        return final