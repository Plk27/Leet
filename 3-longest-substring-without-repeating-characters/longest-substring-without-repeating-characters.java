class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        int maxLength = 0;
        
        // Use a Set for O(1) lookups instead of ArrayList
        Set<Character> seen = new HashSet<>();

        // Expand the right window boundary across the string
        while (right < s.length()) {
            char currentChar = s.charAt(right);

            // If the character is a duplicate, shrink the window from the left
            while (seen.contains(currentChar)) {
                seen.remove(s.charAt(left));
                left++;
            }

            // Add the new unique character and expand right
            seen.add(currentChar);
            right++;

            // Calculate the window size and update our maximum track record
            maxLength = Math.max(maxLength, right - left);
        }

        return maxLength;
    }
}
