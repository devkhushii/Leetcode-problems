class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int,int>> pq;
        unordered_map<int,int> m;
        vector<int> ans;

        for(int i=0;i<nums.size();i++){
            m[nums[i]]++;
        }
        for(auto p:m){
              pq.push({p.second,p.first});
        }
        for(int i=0;i<k;i++){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;
    }
};