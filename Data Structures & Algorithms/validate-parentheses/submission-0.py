class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')' : '(',']' : '[','}' : '{'}

        for i in s:
            if stack and i in mapping.keys():
                brac = stack.pop()
                if brac != mapping[i]:
                    return False 
                else:
                    continue
            stack.append(i)

        if len(stack) != 0:
            return False

        return True


        