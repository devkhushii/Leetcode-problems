class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sl=s.split()

        if len(sl)!=len(pattern):
            return False

        ps={}
        sp={}
        for ph,sh in zip(pattern,sl):
            if ph in ps and ps[ph]!=sh:
                return False
            if sh in sp and sp[sh]!=ph:
                return False
            ps[ph]=sh
            sp[sh]=ph
        return True
        