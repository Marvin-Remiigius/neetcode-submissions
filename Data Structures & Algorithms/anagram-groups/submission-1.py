class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        final_dict = {}
        for word in strs:
            temp_dict = str(Counter(sorted(word)))
            if temp_dict not in final_dict.keys():
                final_dict[temp_dict] = []
            final_dict[temp_dict].append(word)

        return list(final_dict.values())