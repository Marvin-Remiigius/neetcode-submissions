class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in seenMap.keys():
                return [seenMap[nums[i]],i]
            seenMap[difference] = i