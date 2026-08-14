class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        st={}

        max_len=0
        left=0
        for i in range(len(s)):
            
            st[s[i]]=st.get(s[i],0)+1
            while st[s[i]]>2:
                st[s[left]]-=1
                left+=1
            max_len=max(max_len,i-left+1)

            

        return max_len



        