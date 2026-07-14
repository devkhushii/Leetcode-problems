class Solution {
public:
    // int pivotIndex(vector<int>& nums) {
    //     int n = nums.size();

    //     vector<int> left(n);
    //     vector<int> right(n);

    //     left[0] = nums[0];
    //     right[n-1] = nums[n-1];

    //     // Left prefix
    //     for(int i = 1; i < n; i++)
    //         left[i] = left[i-1] + nums[i];

    //     // Right prefix
    //     for(int i = n-2; i >= 0; i--)
    //         right[i] = right[i+1] + nums[i];

    //     for(int i = 0; i < n; i++){

    //         int leftSum = (i == 0) ? 0 : left[i-1];
    //         int rightSum = (i == n-1) ? 0 : right[i+1];

    //         if(leftSum == rightSum)
    //             return i;
    //     }

    //     return -1;
    // }

    int pivotIndex(vector<int>& nums) {

        int total = 0;

        for(int x : nums)
            total += x;

        int leftSum = 0;

        for(int i = 0; i < nums.size(); i++) {

            int rightSum = total - leftSum - nums[i];

            if(leftSum == rightSum)
                return i;

            leftSum += nums[i];
        }

        return -1;
    }
};