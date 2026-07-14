class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> ans(n,0);

        for(int i=0;i<bookings.size();i++){
           int start=bookings[i][0];
           int end=bookings[i][1];
            for(int j=start;j<=end;j++){
                ans[j-1]+=bookings[i][2];
            }
        }
        return ans;
    }
};