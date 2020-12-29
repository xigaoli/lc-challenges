class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        lens=len(s)
        if(k==1):
            return checkPalinDist(s,0,lens-1)
        if(k==lens):
            return 0
        dists = [[0 for _ in range(lens)] for _ in range(lens)]
        for i in range(lens):
            for j in range(i+1,lens):
                dists[i][j]=checkPalinDist(s,i,j)
        memo=[[1000 for _ in range(lens+1)] for _ in range(lens+1)]
        mincost = calcMinCost(dists,lens,k,memo)
        return mincost

def calcMinCost(mx, length, stepsRemaining,memo):
    lengthMinus1=length-1
    if(stepsRemaining==1):
        lastdist=mx[0][lengthMinus1]
        # print("======end here,s={}, lastdist={}".format(s[:length],lastdist))#exit,return cost of s[0,length]
        return lastdist
    mincost=999
    if(memo[lengthMinus1][stepsRemaining] < 999):
        return memo[lengthMinus1][stepsRemaining]

    for k in range(lengthMinus1,stepsRemaining-2,-1):
        #cut at k, current cost = cost(s[0:k] to cut stepsRemaing-1) + cost (s[k:length])
        currCost=calcMinCost(mx,k,stepsRemaining-1,memo)+mx[k][lengthMinus1]
        if(currCost<mincost):
            mincost=currCost
    # print("this level min cost:{}".format(mincost))
    # print("--memo:cut({}) from 0 to {} with {} pieces, mincost={}".format(s[0:length],length-1,stepsRemaining,mincost))
    # min cost at length
    memo[lengthMinus1][stepsRemaining]=mincost
    return mincost

#return how many char need to change to make s1 a palindrome
def checkPalinDist(s1,i,j):
    dist=0
    while True:
        if(i>=j):
            break
        if(s1[i]!=s1[j]):
            dist+=1
        i+=1
        j-=1
    return dist