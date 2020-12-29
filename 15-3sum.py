class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rslt=[]
        nums.sort()
        #rsltDict[a]==False means a does not have answer
        rsltDict=defaultdict(bool)
        
        for i,a in enumerate(nums):
            if(a>0):
                #remaining cannot build a+b+c=0
                break
            if(rsltDict[a]!=False):
                #already solved
                continue
            # now we want b+c=-a
            # twoSum problem, in nums[i:]
            lo=i+1
            hi=len(nums)-1
            while lo<hi:
                if(nums[lo]+nums[hi] + a<0):#too small, increase lo
                    lo+=1
                elif(nums[lo]+nums[hi] + a>0):
                    hi-=1
                else:
                    #found
                    if(rsltDict[a] == False):
                        #new dict
                        rsltDict[a]={nums[lo]:True}
                        rslt.append([a,nums[lo],nums[hi]])
                    elif(nums[lo] not in rsltDict[a].keys()):
                        #existing dict and not exist answer
                        rsltDict[a][nums[lo]]=True
                        rslt.append([a,nums[lo],nums[hi]])
                    lo+=1
                    hi-=1
        return rslt
                    
            