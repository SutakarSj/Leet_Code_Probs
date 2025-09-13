class Solution {
    public int maxSubArray(int[] nums) { 
        int max=Integer.MIN_VALUE;
        int cuz=0;
        int n=nums.length;
        for (int i=0;i<n;i++){
            int temp=cuz+nums[i];
            if (temp<nums[i]){
                cuz=nums[i];
            }
            else{
                cuz=temp;
            }
            if (max<cuz){
                max=cuz;
            }
        } 
        return max;
    }
}
