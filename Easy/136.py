
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        output = 0
        for i in nums:
            output ^= i # XOR
        return output

# print(Solution.singleNumber(Solution, [4,1,2,1,2]))
# 7ms 18.67Mb (38.50% 90.38%)