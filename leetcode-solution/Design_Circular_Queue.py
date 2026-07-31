class MyCircularQueue:

    def __init__(self, k: int):
        """Initializes the object with the size of the queue to be k."""
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.tail = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """Inserts an element into the circular queue. Return true if successful."""
        if self.isFull():
            return False
        
        # Advance tail pointer circularly and insert
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """Deletes an element from the circular queue. Return true if successful."""
        if self.isEmpty():
            return False
        
        # Advance head pointer circularly
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """Gets the front item from the queue. If empty, return -1."""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """Gets the last item from the queue. If empty, return -1."""
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty or not."""
        return self.count == 0

    def isFull(self) -> bool:
        """Checks whether the circular queue is full or not."""
        return self.count == self.capacity
