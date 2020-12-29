class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)#dp means how many ways to decode from s[i:end],including i and end
        ch1=int(s[len(s)-1])
        if(ch1>0):
            dp[len(s)-1]=1
        if(len(s)<=1):#corner case
            return dp[0]

        for idx in range(len(s)-2,-1,-1):
            ch1=int(s[idx])
            w1=0
            if(ch1>0):
                w1=dp[idx+1]    #if only decode 1 ch, dp[12...] has same deocde ways as dp[2...]
            w2=0
            ch2=int(s[idx:idx+2])
            if(ch1>0 and ch2<=26):  #if only decode 2ch, dp[123...] has same decode ways as dp[3...]
                if(idx+2<len(s)):#corner case
                    w2=dp[idx+2]
                else:
                    w2=1
            dp[idx]=w1+w2
        return dp[0]