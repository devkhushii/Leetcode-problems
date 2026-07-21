class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {

        int n = s.size();

        // Count initial active sections (number of 1's)
        int ones = 0;
        for(char c : s)
            if(c == '1')
                ones++;

        // Augment with 1 at both ends
        string t = "1" + s + "1";

        // Store runs: (character, length)
        vector<pair<char,int>> runs;

        for(int i = 0; i < t.size(); ){

            int j = i;

            while(j < t.size() && t[j] == t[i])
                j++;

            runs.push_back({t[i], j - i});

            i = j;
        }

        int gain = 0;

        // Find pattern: 0-run | 1-run | 0-run
        for(int i = 1; i + 1 < runs.size(); i++){

            if(runs[i].first == '1' &&
               runs[i-1].first == '0' &&
               runs[i+1].first == '0'){

                gain = max(gain,
                           runs[i-1].second + runs[i+1].second);
            }
        }

        return ones + gain;
    }
};