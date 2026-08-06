from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _balance(self):
        # Keeps left and right sizes balanced
        # Condition: len(right) >= len(left) and len(right) - len(left) <= 1
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            # Insert into right so right becomes larger by 1
            self.right.appendleft(val)
        else:
            # right is larger, push existing left item deeper, insert new to left
            self.left.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        if not self.left:
            val = self.right.popleft()
        else:
            val = self.left.popleft()
        self._balance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        
        # When lengths match, frontmost middle is the last item of left
        if len(self.left) == len(self.right):
            val = self.left.pop()
        # When right is larger, frontmost middle is the first item of right
        else:
            val = self.right.popleft()
            
        self._balance()
        return val

    def popBack(self) -> int:
        if not self.right:
            return -1
        val = self.right.pop()
        self._balance()
        return val
