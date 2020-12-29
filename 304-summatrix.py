class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #dp[i,j] means the sum of matrix[i,j] to matrix[n-1,n-1]
        #sumregion[x1,y1,x2,y2]=dp[x2+1,y1]-dp[x1,y2+1]-dp[x1,y2]+dp[y2+1,x2+1]
        self.rows=len(matrix)
        if(self.rows>0):
            self.cols=len(matrix[0])
        else:
            self.cols=0
        dp=[[0]*self.cols for _ in range(self.rows)]
        for i in range(self.rows-1,-1,-1):
            for j in range(self.cols-1,-1,-1):
                pass
        print(dp)
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return 0


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)