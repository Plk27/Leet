class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int num=x;
        int reversed =0;
        while(x!=0){
            int ld = x%10;
            reversed = reversed*10 +ld;
            x/=10;
        }
        if(reversed == num){
            return true;
        }
        
        return false;
        
    }
}