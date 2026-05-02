class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        
        lst=[1,2]
        for i in range(2,n):
            lst.append(lst[i-1]+lst[i-2])

        return lst[-1]
        