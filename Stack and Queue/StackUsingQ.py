class MyStack:

    def __init__(self):
        self.q=[]
        self.stack=[]

    def push(self, x: int) -> None:
        while self.stack:
            self.q.append(self.stack.pop(0))
        self.q.append(x)

    def pop(self) -> int:
        if not self.stack:
            while self.q:
                self.stack.append(self.q.pop(0))
        return self.stack.pop()

    def top(self) -> int:
        if self.q:
            return self.q[-1]
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.q and not self.stack


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
