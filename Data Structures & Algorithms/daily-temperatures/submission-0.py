import collections

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = collections.deque()

        for index, temp in enumerate(temperatures):
            if len(stack) == 0 or temp <= stack[-1][0]:
                stack.append((temp, index))
            else:
                while len(stack) > 0 and temp > stack[-1][0]:
                    lower_day = stack.pop()
                    res[lower_day[1]] = index - lower_day[1]
                stack.append((temp, index))

        return res
