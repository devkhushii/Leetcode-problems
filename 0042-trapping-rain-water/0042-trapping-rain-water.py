class Solution:
    def trap(self, height: List[int]) -> int:
        leftmost=[height[0]]*len(height)
        rightmost=[height[len(height)-1]]*len(height)
        left=1
        right=len(height)-2
        water=0
      
     
        while left<len(height) and right>=0:
            leftmost[left] = max(leftmost[left - 1], height[left])
            left+=1

            rightmost[right] = max(rightmost[right + 1], height[right])
            right-=1


        for i in range(len(height)):
            water+=min(leftmost[i],rightmost[i])-height[i]

        return water

