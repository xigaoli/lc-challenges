class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        modnum=10**9+7
        # DP
        # memo[i][steps]= how many ways to move to index 0 when at pos i and have steps left
        # need memo[0][steps]
        # memo[i][steps]= moveleft, stay, moveright
        #               = memo[i-1][steps-1] + memo[i][steps-1] + memo[i+1][steps-1]
        # memo[0][0]=1
        # memo[i][0]=0 when i!=0
        # memo[i][i]=1 because need to move left i steps
        # when i>steps, return 0 because no legal move to idx0
        memo=[[-1]*(steps+1) for _ in range(steps//2+1)]
        def dp(i,currSteps):
            #print(memo)
            if(i==0 and currSteps==0):
                return 1
            if(i!=0 and currSteps==0):
                return 0
            if(i>currSteps or i>=arrLen or i<0 or currSteps<0):
                #invalid/illegal move,no solution
                return 0
            # if(i==currSteps):
            #     return 1
            if(memo[i][currSteps]!=-1): #dp
                return memo[i][currSteps]
            #print("look:i={},currstep={}".format(i,currSteps))
            dleft=dp(i-1,currSteps-1)%modnum
            dstay=dp(i,currSteps-1)%modnum
            dright=dp(i+1,currSteps-1)%modnum
            d=(dleft+dstay+dright)%modnum
            #print("look:i={},currstep={} = {}".format(i,currSteps,d))
            memo[i][currSteps]=d
            return d
        s = dp(0,steps)

        return s