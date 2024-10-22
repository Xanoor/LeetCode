package main

func findMin(nums []int) int {
	var minimum *int
	for i := range nums {
		if minimum == nil || nums[i] < *minimum {
			minimum = &nums[i]
		}
	}
	return *minimum
}

//0ms 4.25Mb (100.00% 7.60%)
