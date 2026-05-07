class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "Stack Underflow"

        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top is None:
            return "Stack is empty"

        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        temp = self.top

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print(s.peek())

print(s.pop())

s.display()
