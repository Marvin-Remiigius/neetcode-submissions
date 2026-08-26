class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = left + ((right - left)//2)

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = 0
                r = len(matrix[mid])-1
                while l <= r:
                    m = l + ((r - l)//2)

                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        r -= 1
                    else:
                        l += 1

                else:
                    return False

            elif target > matrix[mid][-1]:
                left += 1

            else:
                right -= 1

        return False

