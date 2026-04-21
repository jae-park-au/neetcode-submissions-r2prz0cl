import collections
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                num2, num1 = int(stack.pop()), int(stack.pop())
                new_val = self.operate(num1, num2, token)
                stack.append(new_val)

            else:
                stack.append(token)

        return int(stack.pop())

    def operate(self, num1: int, num2: int, operator: str) -> int:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return int(float(num1) / num2)
