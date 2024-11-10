
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [set() for i in range(9)]
        column = [set() for i in range(9)]
        cells = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                box_index = (i // 3) * 3 + (j // 3)
                val = board[i][j]
                if val == ".":
                    continue
                if val in row[i] or val in column[j] or val in cells[box_index]:
                    return False
                row[i].add(val)
                column[j].add(val)
                cells[box_index].add(val)
        return True


# print(Solution.isValidSudoku(Solution, [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
# 3ms 16.64Mb (83.02% 16.64%)