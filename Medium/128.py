
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)<1:
            return 0
        output = 1
        nums = set(nums)
        for i in nums:
            tmp = 1
            if i-1 not in nums:
                while i+tmp in nums:
                    tmp += 1
                output = max(output, tmp)
        return output
    
# print(Solution.longestConsecutive(Solution, [1,0,-1]))
# 48ms 33.40Mb (67.34% 18.53%)



# Solution that do not meet the O(n) complexity constraint -> 0(n log n).
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         if len(nums)<1:
#             return 0
#         output = 1
#         tmp = 1
#         nums.sort()
#         for i in range(1,len(nums)):
#             if nums[i]==nums[i-1]: continue
#             if nums[i]==nums[i-1]+1:
#                 tmp += 1
#                 if tmp > output:
#                     output = tmp
#                 continue
#             tmp = 1
#         return output

# 52ms 30.96Mb (62.32% 93.26%) 
