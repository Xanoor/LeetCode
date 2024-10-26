
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
    
#print(Solution.plusOne(Solution, [9, 9, 9]))
#0ms 16.52Mb (100.00% 39.34%)