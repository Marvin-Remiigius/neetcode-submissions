class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a=[]
        # for i in nums:
        #     a.append(i)
        # for i in a:
        #     if count(i)>=2:
        #         return True
        #     else:
        #         return False


        a = []

        for i in nums:
            if i not in a:
                a.append(i)
            else:
                return True
        return False
