class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> sToT;
        unordered_map<char, char> tToS;

        for (int i = 0; i < s.size(); i++) {

            if (sToT.count(s[i])) {
                if (sToT[s[i]] != t[i])
                    return false;
            } else {
                sToT[s[i]] = t[i];
            }

            if (tToS.count(t[i])) {
                if (tToS[t[i]] != s[i])
                    return false;
            } else {
                tToS[t[i]] = s[i];
            }
        }

        return true;
      
    }
};