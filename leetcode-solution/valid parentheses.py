class Solution:
    def isValid(self, s: str) -> bool:
        k = []
        x = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in x.values():   
                k.append(i)
            else:                      
                if not k or k[-1] != x[i]:
                    return False
                k.pop()

        return not k
