class Solution {
public:
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());

        int prev=nums[0];
        int count=1;

        for(int i=0;i<nums.size();i++){

            if(prev!=nums[i]){
                count++;
                prev=nums[i];
            }
            if(count==3){
                return nums[i];
            }
        }
        return nums[0];

        
    }
};