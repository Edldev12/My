class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        flag=True
        small = min(strs)
        other=[]
        for i in range(len(strs)):
            if strs[i]!=small:
              other.append(strs[i])

        for i in range(len(small)):

            for j in range (len(other)):
                 if small[i]!=other[j][i]:
                    flag=False
            if flag:
                common+=small[i]
            else:
                break
        return common

