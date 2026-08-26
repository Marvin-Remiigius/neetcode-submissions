class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            height = heights[i]

            # Expand to the left
            left = i
            while left > 0 and heights[left - 1] >= height:
                left -= 1

            # Expand to the right
            right = i
            while right < n - 1 and heights[right + 1] >= height:
                right += 1

            # Calculate width & area
            width = right - left + 1
            max_area = max(max_area, height * width)

        return max_area