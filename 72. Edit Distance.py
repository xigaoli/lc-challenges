class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i,j] means edit dist of word1[0...i] to word2[0...j]
        # dp[2,1] -> hor ro
        # if last char same -> dp[i,j] =dp[i-1,j-1]
        # aaa bba -> min(dist(aa,bb) + 0 , dist(aaa,bb)+1, dist(aa,bba)+1)
        # elif last char not same -> dp[i,j] = min (dp[i-1,j]+1, dp[i,j-1]+1, dp[i-1,j-1]+1)
        
        #base case: dp[0,j]=j, dp[i,0]=i (need to add j chars), 
        
        # l1=len(word1)
        # l2=len(word2)
        dp=[ [-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        # for i in range(l1+1):
        #     dp[i][0]=i
        # for j in range(l2+1):
        #     dp[0][j]=j
        
        def helper(i,j):
            if(dp[i][j]!=-1):#memo
                return dp[i][j]
            #calc new stuff
            if(i==0):
                return j
            elif(j==0):
                return i
            if(word1[i-1]==word2[j-1]):#no further bullshit
                dp[i][j] = helper(i-1,j-1)
                
            else: #get min of 3 possibilities
                d1 = helper(i,j-1)+1
                d2 = helper(i-1,j)+1
                d3 = helper(i-1,j-1)+1
                dp[i][j]=min(d1,d2,d3)
                
            return dp[i][j]
        return helper(len(word1),len(word2))