class TextEditor:

    def __init__(self):
        # Characters to the left of the cursor
        self.left = []
        # Characters to the right of the cursor (reversed)
        self.right = []

    def addText(self, text: str) -> None:
        # Appending text means adding characters to the left stack
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        # Delete up to k characters from the left stack
        deleted = 0
        while k > 0 and self.left:
            self.left.pop()
            deleted += 1
            k -= 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        # Move up to k characters from left stack to right stack
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        # Return the last min(10, len(left)) characters
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # Move up to k characters from right stack to left stack
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        # Return the last min(10, len(left)) characters
        return "".join(self.left[-10:])
