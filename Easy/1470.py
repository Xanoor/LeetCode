class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[n+i])
        return output

# print(Solution.shuffle(Solution, nums = [1,2,3,4,4,3,2,1], n = 4))
# 39ms 12.57Mb