class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            if i+nums[i] > farthest:
                farthest = i+nums[i]
            if farthest >= len(nums)-1:
                return True

        return False
    

# print(Solution.canJump(Solution, [2,3,1,1,4]))
# 14ms 13.27Mb