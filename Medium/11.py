
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        total = [0]
        while left < right:
            space = min(height[left], height[right])*(right-left)
            total.append(space)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max(total)


# print(Solution.maxArea(Solution, [1,2,1,3,1,2]))
# 498ms 29.27Mb (89.00% 82.06%)
