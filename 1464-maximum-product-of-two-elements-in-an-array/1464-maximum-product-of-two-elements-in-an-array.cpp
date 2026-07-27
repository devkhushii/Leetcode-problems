class Solution {
public:
    // int maxProduct(vector<int>& nums) {
    //     int maxval=INT_MIN;

    //     for (int i=0;i<nums.size();i++){
    //         for(int j=i+1;j<nums.size();j++){
    //            int val=(nums[i]-1)*(nums[j]-1);
    //            maxval=max(maxval,val); 
    //         }
    //     }
    //     return maxval;
    // }

      int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int maxi1 = INT_MIN;
        int maxi2 = INT_MIN;

        for(int i =0;i<n;i++){
            if(nums[i]> maxi1){
                maxi2 = maxi1;
                maxi1 = nums[i];
            }
            else if(nums[i] > maxi2){
                maxi2 = nums[i];
            }
        }   

        int ans = (maxi1-1)*(maxi2-1);

        return ans;
    }
};