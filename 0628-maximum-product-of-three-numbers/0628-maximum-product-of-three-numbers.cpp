class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        // int maxProd=INT_MIN;
        
        // for(int i=0;i<nums.size();i++){
        //     for(int j=i+1;j<nums.size();j++){
        //         for(int k=j+1;k<nums.size();k++){
        //           int prod=nums[i]*nums[j]*nums[k];
        //           maxProd=max(maxProd,prod);
        //         }
        //     }
        // }
        // return maxProd;
        sort(nums.begin(), nums.end());

        int n = nums.size();

        return max(
            nums[n-1] * nums[n-2] * nums[n-3],
            nums[0] * nums[1] * nums[n-1]
        );
    }
};