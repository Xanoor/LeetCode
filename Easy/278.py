class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start < end:
            middle = start + (end - start) // 2

            if isBadVersion(middle):
                end = middle
            else:
                start = middle+1
        return start


# FIRST VERSION BUT TIME LIMITT EXCEEDED
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         if isBadVersion(n//2):
#             start, end = 0, n//2+1
#         else:
#             start, end = n//2, n+1

#         for i in range(start, end):
#             if isBadVersion(i):
#                 return i
            
#         return 1


# print(Solution.firstBadVersion(Solution, 4))
#33ms 16.60Mb (66.74% 5.60%)