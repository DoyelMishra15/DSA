class MinHeap:
    def __init__(self):
        self.heap = []

    # Parent index
    def parent(self, i):
        return (i - 1) // 2

    # Left child index
    def left(self, i):
        return 2 * i + 1

    # Right child index
    def right(self, i):
        return 2 * i + 2

    # Insert element into heap
    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # Bubble up
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    # Heapify function
    def heapify(self, i):
        smallest = i
        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l

        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    # Get minimum element
    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    # Extract minimum element
    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        # Move last element to root
        self.heap[0] = self.heap.pop()

        # Fix heap
        self.heapify(0)

        return root

    # Decrease key
    def decrease_key(self, i, new_val):
        self.heap[i] = new_val

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    # Delete element at index i
    def delete(self, i):
        self.decrease_key(i, float('-inf'))
        self.extract_min()

    # Print heap
    def print_heap(self):
        print(self.heap)


# Driver code
h = MinHeap()

h.insert(10)
h.insert(20)
h.insert(5)
h.insert(7)
h.insert(1)

h.print_heap()

print("Min:", h.get_min())

print("Extract Min:", h.extract_min())

h.print_heap()

h.delete(1)

h.print_heap()
