class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        #find the array of missing element
        begin = nums[0]
        end=nums[-1]
        miss=0
        if(end-begin-len(nums)+1<k):
            #print("out of range")
            miss=k-(end-begin-len(nums)+1)+end
            return miss
        # print(missingelem)
        
        totalmisscount=0
        for i in range(1,len(nums)):
            d1=nums[i-1]
            d2=nums[i]
            #print("total missed:{}".format(totalmisscount))
            submiss=d2-d1-1 #how many numbers missed between these two nums
            if(totalmisscount+submiss>=k):#happens between d1 + something
                miss=d1+k-totalmisscount
                break
            totalmisscount+=submiss
            
        return miss