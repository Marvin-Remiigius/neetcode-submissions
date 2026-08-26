class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        start = left
        end = right
        while left < right:
            mid = left + ((right - left) // 2) 

            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        cutpoint = left

        if nums[cutpoint] <= target <= nums[end]:
            left = cutpoint
            right = end

            while left <= right :
                mid = left + ((right - left)//2)

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    return mid
                else:
                    left = mid + 1

        else :
            # start < target < nums[cutpoint-1]:
            left = start
            right = cutpoint - 1

            while left <= right :
                mid = left + ((right - left)//2)

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    return mid
                else:
                    left = mid + 1
        return -1
        