class Solution {
    public int minimumOperations(int[] nums) {
        byte soluce = 0;
        for (byte i=0; i < nums.length; i++) {
            if (nums[i] % 3 != 0) {
                soluce++;
            }
        }
        return soluce;
    }
}

// 1ms 41.93Mb