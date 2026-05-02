class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        width=right
        maxarea=area=0

        while left<right:
            h=min(heights[left],heights[right])
            area=h*width
            maxarea=max(maxarea,area)

            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
            width-=1

        return maxarea