from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = deque()

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                open_bracket = stack.pop()
                if brackets[open_bracket] != char:
                    return False

        if len(stack) > 0:
            return False

        return True
        