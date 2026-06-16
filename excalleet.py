class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r=""
        while columnNumber>0:
            columnNumber-=1
            r=chr(columnNumber%26+ord('A'))+r
            columnNumber//=26
        return r
