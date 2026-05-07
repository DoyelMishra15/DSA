class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue element
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} inserted")

    # Dequeue element
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue.pop(0)

    # Front element
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[0]

    # Check if empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display queue
    def display(self):
        print("Queue:", self.queue)


# Driver code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Front element:", q.front())

print("Dequeued:", q.dequeue())

q.display()
