class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
    
        piles.sort()

        left = 1
        right = piles[-1]   # max speed possible

        def eating(p, k):
            total = 0
            for x in p:
                total += math.ceil(x / k)
            return total

        result = piles[-1]

        while left <= right:
            mid = left + ((right - left) // 2)
            hours = eating(piles, mid)

            if hours <= h:
                result = mid           # candidate speed
                right = mid - 1        # try smaller speed
            else:
                left = mid + 1         # need more speed

        return result
        




            