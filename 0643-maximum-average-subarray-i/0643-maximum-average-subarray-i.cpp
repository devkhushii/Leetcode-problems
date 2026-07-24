class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double maxAvg=INT_MIN;
        double sum=0;
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
        double avg=sum/k;
        maxAvg=max(maxAvg,avg);
        int j=0;
        for(int i=k;i<nums.size();i++){
             sum+=nums[i]-nums[j];
             avg=sum/k;
            maxAvg=max(maxAvg,avg);
            j++;
        }
        return maxAvg;
    }
};