class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #basic sol: use another matrix as tmp space
        #advanced: reuse current matrix, use value other than 0 or 1 to represent changed value
        #use -1 for 1->0 cells
        #use 2 for 0->1 cells
                
        def nextState(i,j,n,m):
            #check all neighbors
            neighbors=[(-1,-1),(-1,0),(-1,1),
                      (0,-1),(0,1),
                      (1,-1),(1,0),(1,1)]
            deadneighbor=0
            liveneighbor=0
            for item in neighbors:
                row=i+item[0]
                col=j+item[1]
                if(row>=0 and row<n and col>=0 and col<m):
                    if(board[row][col]==0 or board[row][col]==2):
                        deadneighbor+=1
                    if(board[row][col]==1 or board[row][col]==-1):
                        liveneighbor+=1
            fate=None
            if(board[i][j]==0):
                if(liveneighbor==3):
                    fate=2      #0->1
                else:
                    fate=0      #still dead
                    
            if(board[i][j]==1):
                if(liveneighbor==2 or liveneighbor==3):
                    fate=1      #still live
                if(liveneighbor>3 or liveneighbor<2):
                    fate=-1     #die, 1->0
            
            print("pt[{},{}],dead={},live={},fate={}".format(i,j,deadneighbor,liveneighbor,fate))
            return fate

        n=len(board)
        m=len(board[0])
        
        for i in range(n):
            for j in range(m):
                #check 8 cells around
                fate=nextState(i,j,n,m)
                board[i][j]=fate
        #conversion
        for i in range(n):
            for j in range(m):
                #check 8 cells around
                t= board[i][j]
                if(t==-1):
                    board[i][j]=0
                if(t==2):
                     board[i][j]=1
        