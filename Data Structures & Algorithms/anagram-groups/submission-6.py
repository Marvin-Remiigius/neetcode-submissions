class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import Counter
        final = []
        mapping = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in mapping:
                mapping[key].append(s)
            else:
                mapping[key] = [s]
            
        return list(mapping.values())