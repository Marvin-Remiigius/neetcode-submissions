class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import Counter
        final = []
        mapping = {}
        for s in strs:
            s_dict = Counter(s)

            if frozenset(s_dict.items()) in mapping.keys():
                mapping[frozenset(s_dict.items())].append(s)
            else:
                mapping[frozenset(s_dict.items())] = [s]
        for val in mapping.values():
            final.append(val)

        return final