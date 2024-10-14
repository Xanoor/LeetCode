class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        output = 0
        for i in hours:
            if i >= target:
                output+=1
        return output

#print(Solution.numberOfEmployeesWhoMetTarget(Solution, [0,1,2,3,4], 2))
#42ms 16.44Mb