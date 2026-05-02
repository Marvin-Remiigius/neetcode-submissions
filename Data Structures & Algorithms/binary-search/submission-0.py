class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums,left,right):
            if left>right:
                return -1
            
            mid = left + (right - left) // 2


            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return binary_search(nums,left,mid-1)

            else:
                return binary_search(nums,mid+1,right)


        return binary_search(nums,0,len(nums)-1)
