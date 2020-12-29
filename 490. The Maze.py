class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
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
        visitedSet = set()
        #statequeue has a pt attribute (x,y)
        #each point has 4 dir:
        #(x,y,dir) means this point and the incoming direction
        #use bfs
        heapq.heappush(stateQueue,(0,(start[0],start[1])))
        while True:
            if(len(stateQueue) <=0):
                #print("no find")
                #return false
                return False
            #get pt
            _,pt = heapq.heappop(stateQueue)
            if(pt[0]==destination[0] and pt[1]==destination[1]):
                    #print("found:{}".format(newpt))
                return True
            for d in ["u","d","l","r"]:
                newpt,delta = movedir(maze,d,pt)
                visitedPt=(newpt[0],newpt[1],d)
                if(visitedPt not in visitedSet):
                    visitedSet.add(visitedPt)
                    stateQueue.append((delta,newpt))
        return