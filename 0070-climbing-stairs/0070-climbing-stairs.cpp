class Solution {
public:
    //   vector<int> dp;

    // int solve(int n){

    //     if(n == 1)
    //         return 1;

    //     if(n == 2)
    //         return 2;

    //     if(dp[n] != -1)
    //         return dp[n];

    //     return dp[n] = solve(n - 1) + solve(n - 2);
    // }

    // int climbStairs(int n) {

    //     dp.resize(n + 1, -1);

    //     return solve(n);
    // }
    int climbStairs(int n) {

        if(n == 1)
            return 1;

        int prev2 = 1;   // ways to reach step 1
        int prev1 = 2;   // ways to reach step 2

        for(int i = 3; i <= n; i++){

            int curr = prev1 + prev2;

            prev2 = prev1;
            prev1 = curr;
        }

        return prev1;
    }
};