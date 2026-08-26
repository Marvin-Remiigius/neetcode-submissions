class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        cuns = Counter(s)
        cunt = Counter(t)
        if cuns == cunt:
            return True
        else:
            return False


        