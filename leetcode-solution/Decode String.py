class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        stack = []
        num = 0

        for i in s:
            if i.isdigit():
                num = (num * 10) + int(i)

            elif i == '[':
                stack.append([num, []])
                num = 0
            
            elif i == ']':
                mNum, pList = stack.pop()
                newStr = "".join(pList) * mNum

                if stack:
                    stack[-1][-1].append(newStr)
                else:
                    res.append(newStr)

            else:
                if stack:
                    stack[-1][-1].append(i)
                
                else:
                    res += i

        return "".join(res)
