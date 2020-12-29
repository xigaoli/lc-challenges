
#idea:
# use dict to record seen (prefix)sum so far
# if currentSum ==0 then found one pair, ans+=1
# if currentSum appears in dict:
#   means sum(A[0...j]) == sum(A[0...i]), which means sum(A[j+1...i]) == 0
#   so ans+= dict[currentSum]
#   put currentSum into dict -> dict[currentSum]+=1
#   remember constraints

#only need a dict of len(N) and scanning the array in one pass
#O(N) space and O(N) time

def solution(A):
    seenSumDict={}
    currSum=0
    ans=0
    for item in A:
        currSum+=item
        if(currSum==0):#found one pair
            ans+=1
        if(currSum in seenSumDict):#have compensations
            ans+=seenSumDict[currSum]
        else:#does not have compensations, create new entry for adding
            seenSumDict[currSum]=0
        seenSumDict[currSum]+=1
    if(ans>1000000000):#task constraints
        return -1
    return ans

#two test cases
A=[2,-2,3,0,4,-7]
A=[0 for _ in range(100000)]
print(solution(A))
