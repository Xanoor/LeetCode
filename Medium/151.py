class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s.reverse()
        output = [x for x in s if x != ""]
        return " ".join(output).strip()

#print(Solution.reverseWords(Solution, "a good   example"))
#38ms 16.84Mb (46.60% 25.55%)