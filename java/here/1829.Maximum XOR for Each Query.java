class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int n=nums.length;
        int[] ans=new int[n];
        int k = (1<<maximumBit)-1;
        int pre=0;
        for (int num:nums){
            pre^=num;
        }
        for(int i=0;i<n;i++){
            ans[i]=pre^k;
            pre^=nums[n-1-i];
        }
    return ans;
}
}