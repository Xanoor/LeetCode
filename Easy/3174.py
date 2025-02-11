class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        for i in s:
            if i.isnumeric():
                output = output[:-1]
            else:
                output += i
        return output
    
# print(Solution.clearDigits(Solution, "a44"))
# 2ms 12.35Mb