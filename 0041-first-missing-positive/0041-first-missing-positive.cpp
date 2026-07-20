class Solution {
public:
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