
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                index+=1
                nums[index] = nums[i]
        return index+1
            
#print(Solution.removeDuplicates(Solution, [1,1,2]))
#78ms 17.99Mb (42.10% 52.68%)