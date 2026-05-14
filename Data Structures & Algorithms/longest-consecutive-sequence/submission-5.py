from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        max_len = 0

        if len(nums)==0:
            return 0

        for n in nums:
            length = 0

            while n+length in hashset:
                max_len = max(max_len,length)
                length += 1

        return max_len + 1
