class Solution {
public:
    string smallestPalindrome(string s) {

        vector<int> freq(26, 0);

        // Count frequency
        for (char ch : s)
            freq[ch - 'a']++;

        string left = "";
        char middle = '\0';

        // Build left half
        for (int i = 0; i < 26; i++) {

            left.append(freq[i] / 2, 'a' + i);

            if (freq[i] % 2)
                middle = 'a' + i;
        }

        string right = left;
        reverse(right.begin(), right.end());

        if (middle)
            return left + middle + right;

        return left + right;
    }
};