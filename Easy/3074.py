class Solution:
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        apples = sum(apple)
        counter = 0

        while capacity and apples > 0:
            maxCap = max(capacity)
            apples -= maxCap
            counter += 1
            capacity.remove(maxCap)
        return counter
        

# print(Solution.minimumBoxes(Solution, [1,3,2], [4,3,1,5,2]))
# 0ms 12.23Mb