class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        
        while left < right:
            
            if height[left] < height[right]:
                # update left_max
                left_max = max(left_max, height[left])
                # add water
                water += left_max - height[left]
                # move left pointer
                left += 1
            
            else:
                # update right_max
                right_max = max(right_max, height[right])
                # add water
                water += right_max - height[right]
                # move right pointer
                right -= 1
        
        return water
