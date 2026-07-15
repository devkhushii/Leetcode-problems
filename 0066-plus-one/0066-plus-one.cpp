class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
         for(int i = digits.size() - 1; i >= 0; i--) {

            // If digit is less than 9, simply increment and return
            if(digits[i] < 9) {
                digits[i]++;
                return digits;
            }

            // Digit is 9, becomes 0 and carry moves left
            digits[i] = 0;
        }

        // If we reach here, all digits were 9
        digits.insert(digits.begin(), 1);

        return digits;

    }
};