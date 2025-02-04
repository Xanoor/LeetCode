class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        asc = True
        desc = True
        for i in range(1, len(nums)):
            asc = nums[i] >= nums[i-1] and asc
            desc = nums[i] <= nums[i-1] and desc
            if not asc and not desc:
                break
        return asc or desc
    
# print(Solution.isMonotonic(Solution, [1,3,2]))
# 37ms 20.66Mb