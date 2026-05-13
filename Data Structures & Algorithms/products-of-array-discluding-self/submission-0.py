class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j!= i:
                    product *= nums[j]

            final.append(product)

        return final