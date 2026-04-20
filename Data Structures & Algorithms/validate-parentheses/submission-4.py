import collections

class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()

        brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for char in s:
            if char in brackets.keys():
                stack.append(char)

            else:
                if len(stack) <= 0 or brackets[stack.pop()] != char:
                    return False

        if len(stack) > 0:
            return False

        return True