package main

func searchInsert(nums []int, target int) int {
	for i := range nums {
		if nums[i] >= target {
			return i
		}
	}
	return len(nums)
}

//0ms 4.64Mb (100.00% 6.12%)
