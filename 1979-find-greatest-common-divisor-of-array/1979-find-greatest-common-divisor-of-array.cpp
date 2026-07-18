class Solution {
public:
    int findGCD(vector<int>& nums) {
        int mini=INT_MAX;
        int maxa=INT_MIN;

        for(int i=0;i<nums.size();i++){
            if (nums[i]>maxa){
                maxa=nums[i];
            }
            if (nums[i]<mini){
                mini=nums[i];
            }
        }

        for(int i=mini;i>=0;i--){
            if(mini%i==0 && maxa%i==0){
                return i;
            }
        }
        return 0;
    }
};