package main

func findMin(nums []int) int {
	minimum := nums[0]
	for i := range nums {
		if nums[i] < minimum {
			minimum = nums[i]
		}
	}
	return minimum
}

//0ms 4.66Mb (100.00% 7.14%)
