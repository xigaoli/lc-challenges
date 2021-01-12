class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #maxdeque: max element of array[l,r]
        #mindeque: min element of array[l,r]
        #hold pointer r, shrink pointer l from 0->r
        maxq=deque()
        minq=deque()
        n=len(nums)
        l=0
        res=0
        for r in range(n):
            #construct maxq
            while(len(maxq)>0 and maxq[-1] < nums[r]):
                maxq.pop()#remove anything that smaller than nums[r]
            maxq.append(nums[r])
            
            while(len(minq)>0 and minq[-1] > nums[r]):
                minq.pop()#remove anything that greater than nums[r]
            minq.append(nums[r])
            
            
            #currLimit=limit+1
            while(abs(maxq[0]-minq[0]) >limit):
                    
                if(maxq[0]==nums[l]):
                    maxq.popleft()
                if(minq[0]==nums[l]):
                    minq.popleft()
                l+=1
                #shrink l
            #print("find {} below limit".format([l,r]))
            #now we have [l,r], where fixing r and shrinking l make it fits in limit
            res= max(res, (r-l+1))#update res
        return res