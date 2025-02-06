class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.nums[left:right+1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray([-2, 0, 3, -5, 2, -1])
# param_1 = obj.sumRange(2,5)



# 349ms 15.87Mb