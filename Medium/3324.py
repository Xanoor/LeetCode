
class Solution:
    def stringSequence(self, target: str) -> list[str]:
        output = ["a"]
        index = 0
        while output[-1] != target:
            if output[-1][index] == target[index]:
                output.append(output[-1]+"a")
                index += 1
            else:
                output.append(output[-1][:-1] + chr(ord(output[-1][-1])+1))
        return output
            
# print(Solution.stringSequence(Solution, "he"))
# 19ms 25.88Mb (57.75% 53.26%)

