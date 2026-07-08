class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num

        final = []

        for num in nums:
            if zero_count > 1:
                final.append(0)
            elif zero_count == 1:
                if num == 0:
                    final.append(prod)
                else:
                    final.append(0)
            else:
                final.append(prod // num)

        return final