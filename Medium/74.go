package main

func searchMatrix(matrix [][]int, target int) bool {
	for i := range matrix {
		for v := range matrix[i] {
			if matrix[i][v] == target {
				return true
			}
		}
	}
	return false
}

//0ms 4.14Mb (100.00% 4.14%)
