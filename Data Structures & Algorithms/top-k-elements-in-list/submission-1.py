class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        final = []
        my_dict = Counter(nums)
        my_dict = sorted(my_dict.items(), key=lambda item: item[1])

        my_dict = my_dict[::-1]

        for i in range(k):
            final.append(my_dict[i][0])

        return final
