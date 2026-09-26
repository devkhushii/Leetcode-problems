class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d={}
        for detail in knowledge:
            d[detail[0]]=detail[1]
        
        ans=""
        i=0
        while i<len(s):
            if s[i]=="(":
                w=""
                i+=1
                while s[i]!=")":
                    w+=s[i]
                    i+=1
                
                if w in d:
                    ans+=d[w]
                else:
                    ans+="?"
                    
            else:
                ans+=s[i]
            i+=1
        return ans
                
