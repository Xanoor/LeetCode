class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = -1
        sum_map = {}
        for i in nums:
            num = sum([int(d) for d in str(i)])
            if num in sum_map:
                output = max(output, sum_map[num]+i)
                sum_map[num] = max(sum_map[num], i)
            else:
                sum_map[num] = i        
        return output
    
# print(Solution.maximumSum(Solution, [18,43,36,13,7]))
# 1278ms 21.51Mb