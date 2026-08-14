class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sf={}
        tf={}
        if len(s)!=len(t):
            return False
        for sch, tch in zip(s, t):
            if sch in sf and  sf[sch]!=tch:
                return False
            if tch in tf and tf[tch]!=sch:
                return False
            sf[sch] = tch
            tf[tch] = sch
        return True