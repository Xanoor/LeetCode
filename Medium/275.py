class Solution:
	def hIndex(self, citations: list[int]) -> int:
		n = len(citations)
		left, right = 0, n-1
		hIndex = 0
		while left <= right:
			middle = (left+right)//2
			if citations[middle] >= n - middle:
				hIndex = n-middle
				right = middle-1
			else:
				left = middle+1
		return hIndex

# print(Solution.hIndex(Solution, [0,1,3,5,6, 12, 50, 51, 52, 56, 57]))
# 0ms 22.00Mb (100.00% 95.74%)