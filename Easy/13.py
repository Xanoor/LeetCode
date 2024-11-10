class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1, "Z":0}
        output = 0
        for i in range(len(s)-1):
            if romans[s[i]]<romans[s[i+1]]:
                output -= romans[s[i]]
            else:
                output += romans[s[i]]
        return output + romans[s[-1]]

# print(Solution.romanToInt(Solution, "MCMXCIV"))
# 4ms 16.67Mb (66.12% 38.45%)
