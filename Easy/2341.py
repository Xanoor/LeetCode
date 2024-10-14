class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        output = [0, 0]
        bin = []
        for i in nums:
            if i not in bin:
                output[0] += nums.count(i)//2
                output[1] += nums.count(i)%2
                bin.append(i)
        return output

#print(Solution.numberOfPairs(Solution, [1,3,2,1,3,2,2]))
#34ms 16.7Mb