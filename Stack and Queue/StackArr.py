class Stack:
    def __init__(self):
        self.stack = []

    # Push element
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed")

    # Pop element
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.stack.pop()

    # Peek top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.stack[-1]

    # Check if empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Driver code
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top element:", s.peek())

print("Popped:", s.pop())

s.display()
