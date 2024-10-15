#Two soluces

class Solution: #44ms 16.48Mb (9.94% 67.47%)
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while True:
            if i*i==num: return True
            if i*i > num: return False
            i+=1
        
class Solution: #45ms 16.44 (8.19% 67.47%)
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            if i*i==num: return True
            if i*i > num: return False
        
#print(Solution.isPerfectSquare(Solution, 14))