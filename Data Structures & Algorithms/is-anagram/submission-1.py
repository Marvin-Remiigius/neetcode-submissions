class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for char in s:
            if char not in dict1.keys():
                dict1[char] = 1
            else:
                dict1[char]+=1
                
        for char in t:
            if char not in dict2.keys():
                dict2[char] = 1
            else:
                dict2[char]+=1

        return dict1 == dict2