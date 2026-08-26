class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            if not stack:
                stack.append((i,temp))
                continue
            if temp < stack[-1][1]:
                stack.append((i,temp))
                continue
            else:
                while stack and temp > stack[-1][1]:
                    small_temp = stack.pop()
                    result[small_temp[0]] = i - small_temp[0]
                stack.append((i,temp))

        return result