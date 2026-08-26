class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        new_nums = []
        total_prod = 1
        for i in range(len(nums)):
            new_nums.append(math.prod(nums[:i]+nums[i+1:]))

        return new_nums