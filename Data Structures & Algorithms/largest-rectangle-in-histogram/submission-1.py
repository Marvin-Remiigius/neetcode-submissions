class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices of bars (heights increasing)
        max_area = 0
        n = len(heights)

        for i in range(n):
            # If current height is smaller than stack top → pop and calculate area
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # if stack empty, width extends all the way to i
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)

            stack.append(i)

        # Cleanup pass: treat array end as index n
        while stack:
            h = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, h * width)

        return max_area