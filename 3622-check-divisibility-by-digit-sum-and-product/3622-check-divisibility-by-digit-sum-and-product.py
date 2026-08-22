class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        num=n
        p=1

        while num!=0:
            rem=num%10
            s+=rem
            p*=rem
            num//=10
        
        if n%(s+p)==0 :
            return True
        return False
        