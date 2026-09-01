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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        prefix=[0]*len(matrix[0])
        row=len(matrix)
        col=len(matrix[0])
        max_sum=0
        if not matrix or not matrix[0]:
            return 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=="0":
                    prefix[j]=0
                else:
                    prefix[j]+=1
            max_sum=max(max_sum,self.largestRectangleArea(prefix))
        return max_sum
        