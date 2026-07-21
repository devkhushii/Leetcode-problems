class Solution {
public:
    int longestValidParentheses(string s) {

        stack<int> st;

        st.push(-1);   // Base index

        int ans = 0;

        for(int i = 0; i < s.size(); i++) {

            if(s[i] == '(') {
                st.push(i);
            }
            else {

                st.pop();

                if(st.empty()) {
                    // No matching '(' available,
                    // mark this ')' as new base.
                    st.push(i);
                }
                else {
                    ans = max(ans, i - st.top());
                }
            }
        }

        return ans;
    }
};