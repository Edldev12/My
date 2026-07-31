class MyCircularDeque:

    def __init__(self, k: int):
        """Initializes the deque with a maximum size of k."""
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.tail = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        """Adds an item at the front of Deque. Returns true if successful."""
        if self.isFull():
            return False
        
        # Move head backward circularly before placing value
        self.head = (self.head - 1) % self.capacity
        self.queue[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """Adds an item at the rear of Deque. Returns true if successful."""
        if self.isFull():
            return False
        
        # Place value at current tail, then advance tail circularly
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """Deletes an item from the front of Deque. Returns true if successful."""
        if self.isEmpty():
            return False
        
        # Advance head forward circularly
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """Deletes an item from the rear of Deque. Returns true if successful."""
        if self.isEmpty():
            return False
        
        # Move tail backward circularly
        self.tail = (self.tail - 1) % self.capacity
        self.count -= 1
        return True

    def getFront(self) -> int:
        """Returns the front item from the Deque. Returns -1 if empty."""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        """Returns the last item from Deque. Returns -1 if empty."""
        if self.isEmpty():
            return -1
        # The tail pointer always targets the next empty spot
        return self.queue[(self.tail - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """Returns true if the deque is empty, or false otherwise."""
        return self.count == 0

    def isFull(self) -> bool:
        """Returns true if the deque is full, or false otherwise."""
        return self.count == self.capacity
