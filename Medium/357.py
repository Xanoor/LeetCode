#Three soluces

#36ms 16.58Mb (52.72% 22.16%)
class Solution: 
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        output = 10
        if n == 0: return 1
        if n == 1: return output
        unique_digits = 9
        available_numbers = 9

        for i in range(2, n + 1):
            unique_digits *= available_numbers 
            output += unique_digits  
            available_numbers -= 1  
        return output

#Smart one :D 26ms 16.53Mb (95.22% 22.16%)
class Solution: 
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        possibilities = [1,10,91,739,5275,32491,168571,712891,2345851,5611771,8877691,8877691,8877691,8877691,8877691]
        return possibilities[n]

#print(Solution.countNumbersWithUniqueDigits(Solution, 3))



#First one but too long
class Solution: 
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        output = 0
        if n == 0: return 1

        for i in range(10**n):
            nlist = list(str(i))
            if len(set(nlist)) == len(nlist): output+=1
        return output

