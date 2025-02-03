class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum ([x for x in range(1, n+1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0])
    
# print(Solution.sumOfMultiples(Solution, 7))
# 27ms 12.42Mb