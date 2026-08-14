class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m={}
        for ch in magazine:
            m[ch]=m.get(ch,0)+1
        
        for ch in ransomNote:
            if ch in m:
                m[ch]-=1
            else:
                return False
        
        for key,val in m.items():
            if val<0:
                return False
        return True


        