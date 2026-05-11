class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for index,num in enumerate(nums):

            difference = target - num

            if difference in seenMap:
                return [seenMap[difference],index]
            seenMap[num] = index