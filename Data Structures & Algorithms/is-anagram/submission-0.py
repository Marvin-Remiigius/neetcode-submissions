class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        dict1 = Counter(s)
        dict2 = Counter(t)

        return dict1 == dict2