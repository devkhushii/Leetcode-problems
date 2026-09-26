class Solution:
    
    def partition(self, s: str) -> list[list[str]]:

        def isPallindrome(st):
            left=0
            right=len(st)-1
            while left<right:
                if st[left]!=st[right]:
                    return False
                left+=1
                right-=1
            return True

        ans=[]
        partition=[]

        def backtrack(st,ans,partition):
            i=0
            if i==len(st):
                ans.append(partition[:])
                return 
            
            while i<len(st):

                part=st[0:i+1]
                if isPallindrome(part):
                    partition.append(part)
                    backtrack(st[i+1:],ans,partition)
                    partition.pop()
                i+=1

        backtrack(s,ans,partition)
        return ans


        