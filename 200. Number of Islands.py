class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandMap=[[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        if(len(grid)==0):
            return 0
        
        #print(islandMap)
        currIslandNum=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #new land and not marked belong to some island
                if(grid[i][j]=="1" and islandMap[i][j]==0):
                    self.searchIslandFromPoint(i,j,currIslandNum,grid,islandMap)
                    currIslandNum+=1
                    
        return currIslandNum-1
    def searchIslandFromPoint(self,x,y,currIslandNum,grid,islandMap):
        #search horizontally
        islandMap[x][y]=currIslandNum
        for i in range(y+1,len(grid[x])):
            
            if(grid[x][i] != "0" and islandMap[x][i]==0):
                islandMap[x][i]=currIslandNum
                self.searchIslandFromPoint(x,i,currIslandNum,grid,islandMap)
            else:
                break
        #search horizontally, rev
        for i in range(y-1,-1,-1):
            if(grid[x][i] != "0" and islandMap[x][i]==0):
                islandMap[x][i]=currIslandNum
                self.searchIslandFromPoint(x,i,currIslandNum,grid,islandMap)
            else:
                break
        
        #search vertically
        for j in range(x+1,len(grid)):
            if(grid[j][y] !="0" and islandMap[j][y]==0):
                islandMap[j][y]=currIslandNum
                self.searchIslandFromPoint(j,y,currIslandNum,grid,islandMap)
            else:
                break
        #search vertically,rev
        for j in range(x-1,-1,-1):
            if(grid[j][y] !="0" and islandMap[j][y]==0):
                islandMap[j][y]=currIslandNum
                self.searchIslandFromPoint(j,y,currIslandNum,grid,islandMap)
            else:
                break