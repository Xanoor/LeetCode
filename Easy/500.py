
class Solution:
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    def findWords(self, words: list[str]) -> list[str]:
        output = []
        for i in words:
            row1 = True
            row2 = True
            row3 = True
            for l in i:
                if l.lower() not in Solution.rows[0]:
                    row1 = False
                if l.lower() not in Solution.rows[1]:
                    row2 = False
                if l.lower() not in Solution.rows[2]:
                    row3 = False
            if row1 or row2 or row3:
                output.append(i)
        return output
    
# print(Solution.findWords(Solution, ["Hello","Alaska","Dad","Peace"]))
# 0ms 16.50Mb (100.00% 76.63%)





# SECOND SOLUTION (0ms 16.52Mb (100.00% 39.45%))

# class Solution:
#     rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
#     def findWords(self, words: list[str]) -> list[str]:
#         row = None
#         output = []
#         for i in words:
#             if i[0].lower() in Solution.rows[0]:
#                 row = Solution.rows[0]
#             elif i[0].lower() in Solution.rows[1]:
#                 row = Solution.rows[1]
#             else:
#                 row = Solution.rows[2]
#             for l in i:
#                 if l.lower() not in row:
#                     row = None
#                     break
#             if row != None:
#                 output.append(i)
#         return output