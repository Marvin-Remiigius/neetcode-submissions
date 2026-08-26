class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1 
        output = [0]*len(nums)
        for i in range(len(nums)):
            output[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1

        for i in range(len(nums)-1,-1,-1):
            output[i] *= suffix_product
            suffix_product *= nums[i]

    
        return output