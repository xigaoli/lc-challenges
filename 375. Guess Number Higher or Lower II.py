class Solution:
    def getMoneyAmount(self, n: int) -> int:
        #dp
        #dp[i][j] means min cost of number range from [i,j]
        #dp[i][j]=min(dp[i][k-1]+k+dp[k+1][j])
        #if(i+1==j): dp[i][j]=i
        #dp[i,i]=0 ??
        dp=[0]*(n+1)
        #print(dp)
        for i in range(n+1):
            dp[i]=[-1]*(n+1) 
            dp[i][i]=0
            if(i+1<=n):
                dp[i][i+1]=i

        def helper(i,j):
            #print("calculate dp[{},{}]".format(i,j))
            if(dp[i][j]!=-1):
                #already calculated
                return dp[i][j]
            #not calc-ed
            # if(i+1==j):#base case 1
            #     dp[i][j]=i
            #     return dp[i][j]
            # if(i==j):
            #     dp[i][j]=0
            #     return dp[i][j]
            #other case
            mincost=9999 # max is 1+2+...+200
            mid=(i+j)//2
            for k in range(mid,j):
                #guess k
                low = helper(i,k-1)#if ans is low
                high = helper(k+1,j)#if ans is high
                newcost= max(low,high) + k
                if(newcost<mincost):
                    mincost=newcost
            dp[i][j]=mincost
            return dp[i][j]
        rslt = helper(0,n)
            
        
        return rslt