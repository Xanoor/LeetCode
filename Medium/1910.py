class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        l = len(part)
        while part in s:
            i = s.index(part)
            s = s[:i]+s[i+l:]

        return s


# print(Solution.removeOccurrences(Solution, "axxxxyyyyb", "xy"))
# 0ms 12.46Mb