class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        if len(nums)%2 != 0: return False
        for i in nums:
            if nums.count(i)>2: return False
        return True

#print(Solution.isPossibleToSplit(Solution, [1, 2, 2, 4]))
#48ms 16.43Mb (45.50% 77.16%)