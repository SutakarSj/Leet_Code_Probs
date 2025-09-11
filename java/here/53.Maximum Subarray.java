class Solution {
    public int maxSubArray(int[] nums) {
        //finding maximum subarray using kadane's algorithm method one 
        /*int max=nums[0];
        int cuz=0;
        for (int n:nums){
            cuz = Math.max(cuz,0);
            cuz=cuz+n;
            max = Math.max(cuz,max);
        }
        return max;
    }*/
    //method two 
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