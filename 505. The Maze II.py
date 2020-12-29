class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        #dirx=[[999999]*len(maze[0]) for _ in range(len(maze))]
        def movedir(maze,d,pt):
            newx=pt[0]
            newy=pt[1]
            delta=0
            while True:
                if(d=="u"):
                    if(newx-1<0 or maze[newx-1][newy]==1):
                        break
                    newx-=1
                elif(d=="d"):
                    if(newx+1>=len(maze) or maze[newx+1][newy]==1):
                        break
                    newx+=1
                elif(d=="l"):
                    if(newy-1<0 or maze[newx][newy-1]==1):
                        break
                    newy-=1
                else:
                    if(newy+1>=len(maze[0]) or maze[newx][newy+1]==1):
                        break
                    newy+=1
                delta+=1
            #print("newx={},newy={}".format(newx,newy))
            return (newx,newy),delta
        
        stateQueue=[]
        visitedSet=set()
        #statequeue has a pt attribute (x,y)
        #use bfs
        heapq.heappush(stateQueue,(0,(start[0],start[1])))
        while True:
            if(len(stateQueue) <=0):
                #print("no find")
                #return false
                return -1
            #get pt
            s0,pt = heapq.heappop(stateQueue)
            visitedSet.add(pt)
            if(pt[0]==destination[0] and pt[1]==destination[1]):
                #print("found:{}".format(newpt))
                return s0
            for d in ["u","d","l","r"]:
                newpt,delta = movedir(maze,d,pt)
                if(delta==0):
                    continue
                s1=s0+delta
                if(newpt not in visitedSet):#only walk with shortest dist
                    #update shortest path
                    # dirx[newpt[0]][newpt[1]]=s1
                    heapq.heappush(stateQueue,(s1,newpt))