class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n=len(s)
        def lps_compute(pattern):
            m=len(pattern)
            lps=[0]*m
            length=0
            i=1
            while i<m:
                if pattern[i]==pattern[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                elif length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1
            return lps

            
        rev=s[::-1]
        combine=s+"#"+rev
        lps=lps_compute(combine)  
        prefix_len = lps[-1]
        remaining=s[prefix_len:]
        return remaining[::-1]+s     