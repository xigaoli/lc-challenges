class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use compensate
        #key = number, value = index
        cdict={}
        for i,n in enumerate(nums):
            comp = target-n
            if(comp in cdict.keys()):
                idx = cdict[comp]
                return [i,idx]
            #print("{}-no".format(n))
            cdict[n]=i
            #print(cdict)
            