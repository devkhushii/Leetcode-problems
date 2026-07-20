class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans(2,-1);

    int left=0;
    int right=nums.size()-1;

    while(left<=right){

        int mid=left+(right-left)/2;

        if(nums[mid]==target){

            int first=mid;
            int last=mid;

            while(first>=0 && nums[first]==target)
                first--;

            while(last<nums.size() && nums[last]==target)
                last++;

            ans[0]=first+1;
            ans[1]=last-1;

            return ans;
        }

        else if(nums[mid]>target)
            right=mid-1;

        else
            left=mid+1;
    }

    return ans;
    }
};