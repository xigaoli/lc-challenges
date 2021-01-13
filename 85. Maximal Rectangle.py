class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        if(n==0):
            return 0
        m=len(matrix[0])
        
        
        for j in range(m):
            cnt=0
            for i in range(n):
                if(matrix[i][j]=='1'):
                    cnt+=1
                else:
                    cnt=0
                matrix[i][j]=cnt
        maxarea=0
        for row in matrix:
            #print(row)
            area = self.lc84_largestRectangleArea(row)
            maxarea=max(maxarea,area)
        return maxarea
    def lc84_largestRectangleArea(self, heights: List[int]) -> int:
        if(len(heights)==0):
            return 0
        #use stack
        st = deque()    #store the index of stuff
        st.append(-1)
        maxarea=0
        for i in range(len(heights)):
            item=heights[i]
            if(len(st)==1 or item>=heights[st[-1]]):
                #push in
                st.append(i)
            else:
                #calc and pop
                #print("pop at {}({})".format(i,heights[i]))
                while( len(st)>1 and item<heights[st[-1]]):
                    currheight=heights[st[-1]]
                    st.pop()
                    idx=st[-1]
                    area=currheight*(i-idx-1)
                    maxarea=max(area,maxarea)
                    #print("area [{},{}]={}".format(idx,i,area))
                st.append(i)
        #print(st)
        lastpt=len(heights)
        while(len(st)>1):
            currheight=heights[st[-1]]
            st.pop()
            idx=st[-1]
            area=currheight*(lastpt-idx-1)
            maxarea=max(area,maxarea)
            #print("area [{},{}]={}".format(idx,lastpt,area))
        return maxarea