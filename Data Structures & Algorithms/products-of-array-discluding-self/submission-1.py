class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        new_nums = []
        total_prod = 1
        for i in range(len(nums)):
            total_prod *= nums[i]
    
        for i in range(len(nums)):
            print(i)
            if nums[i] == 0 :
                print("running")
                new_nums.append(math.prod(nums[:i]+nums[i+1:]))
    
            else:
                new_nums.append(int(total_prod/nums[i]))
        return new_nums