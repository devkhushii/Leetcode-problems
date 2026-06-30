class Solution {
public:
    int characterReplacement(string s, int k) {
        int freq[26] = {0};
    int left = 0, maxFreq = 0, result = 0;
    
    for (int right = 0; right < s.length(); right++) {
        freq[s[right] - 'A']++;
        maxFreq = max(maxFreq, freq[s[right] - 'A']);
        
        // Window invalid: replacements needed > k
        while ((right - left + 1) - maxFreq > k) {
            freq[s[left] - 'A']--;
            left++;
            // Note: we don't update maxFreq (lazy deletion optimization)
        }
        result = max(result, right - left + 1);
    }
    return result;
    }
};