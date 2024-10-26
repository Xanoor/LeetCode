package main

func findPeakElement(nums []int) int {
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] && (i == len(nums)-1 || nums[i] > nums[i+1]) {
			return i
		}
	}
	return 0
}

//0ms 4.48Mb (100.00% 10.43%)
