class Solution {
public:
    // int firstMissingPositive(vector<int>& nums) {
    //    int n = nums.size();
    //     //cyclic sort
    //     for(int i = 0; i < n; i++){
    //         while(nums[i] > 0 && nums[i] <= n && nums[i] != nums[nums[i] - 1]){
    //             swap(nums[i] , nums[nums[i] - 1]);
    //         }
    //     }

    //     for(int i = 0; i < n; i++){
    //         if(nums[i] != i + 1){
    //             return i + 1;
    //         }
    //     }
    //     return n + 1;
    // }

       int firstMissingPositive(vector<int>& nums) {

        unordered_set<int> s(nums.begin(), nums.end());

        int i = 1;

        while (true) {
            if (s.find(i) == s.end()) {
                return i;
            }
            i++;
        }
    }
};