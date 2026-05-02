class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            if not stack:
                stack.append((i,temp))
                continue
            if temp <= stack[-1][1]:
                stack.append((i,temp))

            else:
                while stack and temp > stack[-1][1]:
                    smaller_index = stack.pop()[0]
                    diff = i - smaller_index
                    result[smaller_index] = diff
                stack.append((i,temp))

        return result



