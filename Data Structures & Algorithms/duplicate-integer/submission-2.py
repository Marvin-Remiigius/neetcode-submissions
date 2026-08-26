class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        nums_set = set(nums)

        return not len(nums_set) == len(nums)