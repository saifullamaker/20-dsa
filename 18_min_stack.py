# Design a stack that can return its minimum in O(1) time

class MinStack:
    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, value):
        self.stack.append(value)
        if not self.minimums or value <= self.minimums[-1]:
            self.minimums.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.minimums[-1]:
            self.minimums.pop()
        return value

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.minimums[-1] if self.minimums else None


if __name__ == "__main__":
    stack = MinStack()
    stack.push(5)
    stack.push(2)
    stack.push(7)
    print("Top:", stack.top())
    print("Minimum:", stack.get_min())
    stack.pop()
    print("Minimum after pop:", stack.get_min())
