import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select, similar as quick partition
        n=len(nums)
        def partition(lo,hi,pivotidx):
            pivot=nums[pivotidx]#store to rightmost
            nums[pivotidx]=nums[hi]
            nums[hi]=pivot
            storeidx=lo
            for i in range(lo,hi):#move all thing smaller than pivot to left
                if(nums[i]<pivot):
                    #swap nums[i] and nums[storeidx], then storeidx+=1: textbook
                    nums[i],nums[storeidx] = nums[storeidx],nums[i]
                    storeidx+=1
            
            #swap pivot with storeidx
            nums[storeidx], nums[hi] = nums[hi],nums[storeidx]
            #finish partition, this is the place pivot should be
            #pivot at storeidx-th place
            return storeidx
        
        def qsel(lo,hi,target):
            #choose pivot = (hi-lo)//2
            #move all item >pivot to right
            #random.seed(10)
            pivot_idx = random.randint(lo,hi)#lo<=idx<=hi
            pivot_val=nums[pivot_idx]
            new_idx = partition(lo,hi,pivot_idx)
            #print("pivot={},new arr:{},idx={}".format(pivot_val,nums,new_idx))
            if(new_idx==target):
                #found
                return pivot_val
            if(new_idx<target):
                #need to find on right side,[new_idx+1,hi]
                #print("right")
                val = qsel(new_idx+1,hi,target)
                return val
            else:
                #[lo,new_idx-1]
                #print("left")
                val = qsel(lo,new_idx-1,target)
                return val
                
        
        target=n-k
        #print("target={}th elem".format(target))
        val = qsel(0,n-1,target)
        return val