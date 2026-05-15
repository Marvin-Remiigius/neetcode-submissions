class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        my_dict = Counter(nums)

        my_dict = list(my_dict.items())

        my_dict = sorted(my_dict, key = lambda item : item[1],reverse = True)

        return list(x[0] for x in my_dict[:k]) 

        
            