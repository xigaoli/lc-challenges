class Solution:
    def shortestPath(self, grid, k) -> int:
        
        visited=set((0,0,k))
        stepsqueue=collections.deque()
        stepsqueue.append((0,0,0,0))
        while len(stepsqueue)>0:
            #
            v,h,k0,s0 = stepsqueue.popleft()
            if(v==len(grid)-1 and h==len(grid[0])-1):
                        return s0
            #down, right, up, left
            for v1,h1 in [(v+1,h),(v,h+1),(v-1,h),(v,h-1)]:
                if (v1>=0 and h1>=0 and v1<len(grid) and h1 <len(grid[0])):
                    s1=s0+1
                    if(grid[v1][h1]==1):
                        k1=k0+1
                        if(k1>k):
                            continue
                    else:
                        k1=k0
                    newpt = (v1,h1,k1)
                    if(newpt in visited):
                        continue
                    if(v1==len(grid)-1 and h1==len(grid[0])-1):
                        return s1
                    #add into visited
                    visited.add((v1,h1,k1))
                    stepsqueue.append((v1,h1,k1,s1))
        return -1