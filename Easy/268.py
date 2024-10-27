#Low memory

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(max(nums)):
            if i not in nums:
                return i
        return len(nums)

#print(Solution.missingNumber(Solution, [0,1]))
#1366ms 17.59Mb (5.00% 98.49%)