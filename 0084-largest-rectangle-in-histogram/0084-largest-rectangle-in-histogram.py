class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n=len(heights)
        right=[0]*n
        left=[0]*n

        for i in range(n-1,-1,-1):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            else:
                right[i]=n
            stack.append(i)
        stack=[]   
        for i in range(n):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            else:
                left[i]=-1
            stack.append(i)
        
        for i in range(n):
            h=heights[i]
            w=right[i]-left[i]-1
            max_area=max(max_area,h*w)

        return max_area