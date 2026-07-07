class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        for i,num in enumerate(nums):
            diff = target - num
            if num in seenMap:
                return [seenMap[num],i]
            seenMap[diff] = i