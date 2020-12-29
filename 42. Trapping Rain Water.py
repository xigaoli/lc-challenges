class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        prevHeight=0
        prevIndex=0
        if(len(height)==0):
            return 0
        # for i,h in enumerate(height):
        #     if(h>=prevHeight):
        #         prevIndex=i
        #         prevHeight=h
        #left -> right
        #stopPt=prevIndex
        # prevHeight=0
        # prevIndex=0
        currObstacle=0
        for i,heightNum in enumerate(height):
            #heightNum=height[i]
            # print("[{}] height={}".format(i,heightNum))
            # if(prevHeight==0):
            #     prevIndex=i
            #     prevHeight=heightNum
            #     continue
            if(prevHeight!=0 and prevHeight>heightNum):
                ##can add water, become obstacle
                currObstacle+=heightNum
            else:
                #become a pool
                dist=i-prevIndex-1
                if(prevHeight!=0 and dist!=0):
                    water+=prevHeight*dist-currObstacle
                prevIndex=i
                prevHeight=heightNum
                currObstacle=0
        #right->left
        stopPt=prevIndex
        prevHeight=0
        currObstacle=0
        for i in range(len(height)-1,stopPt-1,-1):
            heightNum=height[i]
            # print("[{}] height={}".format(i,heightNum))
            # if(prevHeight==0):
            #     prevIndex=i
            #     prevHeight=heightNum
            #     continue
            if(prevHeight!=0 and prevHeight>heightNum):
                ##can add water, become obstacle
                currObstacle+=heightNum
            else:
                #become a pool
                dist=prevIndex-i-1
                if(prevHeight!=0 and dist!=0):
                    water+=prevHeight*dist-currObstacle
                prevIndex=i
                prevHeight=heightNum
                currObstacle=0
        return water