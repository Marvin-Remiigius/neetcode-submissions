class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','/','*']
        stack = []

        for i in tokens:
            if i not in operators:
                stack.append(int(i))

            if i == '+':
                operand_1 = stack.pop()
                operand_2 = stack.pop()

                stack.append(operand_2 + operand_1)

            if i == '-':
                operand_1 = stack.pop()
                operand_2 = stack.pop()

                stack.append(operand_2 - operand_1)


            if i == '*':
                operand_1 = stack.pop()
                operand_2 = stack.pop()

                stack.append(operand_2 * operand_1)


            if i == '/':
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                if operand_1 != 0:
                    stack.append(int(operand_2 / operand_1))

                else:
                    raise Exception("Zero Division Error")

        if len(stack)!= 1:
            return "Stack Not Empty"

        return stack.pop()