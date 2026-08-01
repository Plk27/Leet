class Solution {
    public boolean canJump(int[] nums) {
        int maxReachable = 0;
        
        for (int i = 0; i < nums.length; i++) {
            // If the current index is further than your max reach, 
            // it means you got stuck at a previous 0 and can't go further.
            if (i > maxReachable) {
                return false;
            }
            
            // Update your max reach from the current position
            maxReachable = Math.max(maxReachable, i + nums[i]);
            
            // Optimization: If you can already reach the last index, stop early
            if (maxReachable >= nums.length - 1) {
                return true;
            }
        }
        
        return true;
    }
}
