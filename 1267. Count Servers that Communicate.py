class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        totalSrv=0
        #col
        singleRowIdx=set()
        
        #col->row
        for i in range(len(grid)):
            #row
            currentRowSrvCount=0
            # FalsePositive=False
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    totalSrv+=1
                    currentRowSrvCount+=1
                    prevColIdx=j
                    if(prevColIdx in singleRowIdx):
                        singleRowIdx.remove(prevColIdx)
                        # FalsePositive=True
            if(currentRowSrvCount==1):
                #suspicious
                singleRowIdx.add(prevColIdx)
        # print("totalSrv={}, singleRowIdx={}".format(totalSrv,singleRowIdx))

        #row->col
        for colNum in singleRowIdx:
            currentColSrvCount=0
            isIsolated=1
            #check if they have only one server in this col
            # check if grid[i][colnum] have only one server
            for i in range(len(grid)):
                if(grid[i][colNum]==1):
                    currentColSrvCount+=1
                if(currentColSrvCount>1):
                    isIsolated=0
                    break
            #if(currentColSrvCount==1):
                # print("isolated server, at {},{}".format(tmpRowNum,colNum))
            #currentColSrvCount can only be 0 or 1 when reach here
            totalSrv-=isIsolated

        return totalSrv
                    