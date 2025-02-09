class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [celsius+273.15, celsius*1.8+32]
    
# print(Solution.convertTemperature(Solution, 36.5))
# 0ms 12.48Mb