class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #island expansion
        landcount=2
        n=len(grid)
        if(n==0):
            return 0
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        m=len(grid[0])
        
        def expand_island(i,j,landnum):
            #expand the island from point i,j (only if pt[i,j]==1)
            #return how much area it expanded from i,j
            area = 0
            if(i<0 or j<0 or i>n-1 or j>m-1):
                #oob, nothing to expand
                return 0
            if(grid[i][j]==1):
                area=1
                grid[i][j]=landnum
                #4 directions
                for d in directions:
                    i1=i+d[0]
                    j1=j+d[1]
                    #print("exp: {},{},land={}".format(i1,j1,landnum))
                    rslt = expand_island(i1,j1,landnum)
                    #print("exp: {},{},land={},rslt={}".format(i1,j1,landnum,rslt))
                    area+=rslt
                return area
            else:
                return 0
        maxarea=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    area = expand_island(i,j,landcount)
                    maxarea = max(area,maxarea)
                    #print("exp {},{},land={},area={}".format(i,j,landcount,area))
                    landcount+=1

        return maxarea