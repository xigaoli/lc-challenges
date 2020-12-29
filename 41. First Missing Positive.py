from collections import defaultdict
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numdict = defaultdict(int)
        for n in nums:
            #print(n)
            numdict[n]+=1
        for i in range(1,len(nums)+1):
            if(numdict[i]==0):                
                return i
        #if nums is [1,2,...k] then len(nums)+1==k+1 is answer
        return len(nums)+1
            