class Solution:
    def possibleStringCount(self, word: str) -> int:
        output = 1
        last = None
        for s in word:
            if last == s:
                output+=1
            last = s
        return output

#print(Solution.possibleStringCount(Solution, "aaaa"))
#34ms 16.57Mb (100.00% 100.00%)