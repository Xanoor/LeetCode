class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        actual = min(strs)
        for i in range(len(strs)):
            for k in range(len(strs[i])):
                try:
                    if strs[i][k] != actual[k]:
                        actual = actual[:k]
                        break
                except:
                    break
        return actual
    
#print(Solution.longestCommonPrefix(Solution, ["reflower","flow","flight"]))
#29ms 16.60Mb (94.66% 77.77%)