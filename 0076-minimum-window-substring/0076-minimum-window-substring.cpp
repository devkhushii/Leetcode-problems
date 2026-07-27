class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char,int> mp;
        int minWindow=INT_MAX;
        int i=0;
        int j=0;
        int n=s.length();
        if(s.length()<t.length()){
            return "";
        }
        for (auto ch:t){
            mp[ch]++;
        }
        int start_i=0;
        int countRequired=t.size();
        while (j<n){
            char ch=s[j];
            if (mp[ch]>0){
                countRequired--;
            }
            mp[ch]--;

            while(countRequired==0){
                int currentWindowSize=j-i+1;
                
                if (minWindow>currentWindowSize){
                minWindow=min(minWindow,currentWindowSize);
                start_i=i;
                }
                mp[s[i]]++;
                if(mp[s[i]]>0){
                   countRequired++;
                }
                i++;
            }
            j++;
        }

        if (minWindow==INT_MAX){
            return "";
        }else{
            return s.substr(start_i,minWindow);
        }
        
    }
};