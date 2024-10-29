class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = set()
        for i in nums:
            if i in n:
                return i
            n.add(i)
        return nums[-1]
    
# print(Solution.findDuplicate(Solution, [1, 2, 3, 4, 5, 4, 6]))
# 24ms 33.37Mb (72.70% 13.83%)