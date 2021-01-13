class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        #dp[i] means prob to win at step i
        #draw at most K times
        #dp[m]=1 when K=<m<=N
        #dp[i]=1/W(dp[k+1]+...+dp[k+w])
        dp=[0]*(N+W+1)
        for i in range(N+1):
            if(K<=i<=N):
                dp[i]=1.0
        s=0
        for j in range(K,N+1):
            s+=dp[j]
            
            
        for i in range(K-1,-1,-1):
            dp[i]=s/float(W)
            s=s+dp[i]-dp[i+W]
        return dp[0]