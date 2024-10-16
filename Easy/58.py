
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(' ')
        return len(s[-1])

#print(Solution.lengthOfLastWord(Solution, "   fly me   to   the moon  "))
#22ms 16.67Mb (99.07% 21.76%)