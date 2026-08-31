class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        n=len(height)
        right=n-1
        leftmax=0
        rightmax=0
        ans=0
        while left<right:
            leftmax=max(leftmax,height[left])
            rightmax=max(rightmax,height[right])

            if leftmax<rightmax:
                ans+=leftmax-height[left]
                left+=1
            else:
                ans+=rightmax-height[right]
                right-=1

        return ans
        