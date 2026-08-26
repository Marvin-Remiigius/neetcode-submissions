class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op1+op2)
                continue
            if token == "-":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op2 - op1)
                continue
            if token == "*":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op2 * op1)
                continue
            if token == "/":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(int(op2 / op1))
                continue
            stack.append(int(token))
        return stack[-1]