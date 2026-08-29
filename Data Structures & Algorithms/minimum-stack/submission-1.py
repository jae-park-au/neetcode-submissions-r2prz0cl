class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))

        else:
            prev_min = self.stack[-1][1]
            if prev_min < val:
                self.stack.append((val, prev_min))
            else:
                self.stack.append((val, val))

    def pop(self) -> None:
        if len(self.stack) > 0:
            return_tuple = self.stack.pop()
            return return_tuple[0]

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
