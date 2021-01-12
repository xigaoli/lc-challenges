class Solution:

    def __init__(self, w: List[int]):
        self.presum = [0]*len(w)
        addsum=0
        for i in range(len(w)):
            addsum+=w[i]
            self.presum[i]=addsum
        #print(self.presum)

    def pickIndex(self) -> int:
        #bin search the lower bound
        n=len(self.presum)
        target = self.presum[-1]*random.random()
        #print(target)
        #find smallest index larger than bound
        
        
        def find_upper_bound_bin(arr,target):
            lo=0
            hi=len(arr)-1
            
            while(lo<hi):
                mid=lo+(hi-lo)//2
                #print("lo={},hi={},mid={}".format(lo,hi,mid))
                if(arr[mid]<target):
                    lo=mid+1
                    if(arr[lo]>=target):
                        #corner end
                        break
                else:
                    hi=mid
            #print(lo)
            return lo

        def find_upper_bound(arr,target):
            if(arr[0]>target):
                return 0
            for i in range(1,len(arr)):
                if(i>0 and arr[i-1]<target and arr[i]>=target):
                    return i
            return len(arr)-1
        rslt = find_upper_bound_bin(self.presum,target)
        return rslt
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()