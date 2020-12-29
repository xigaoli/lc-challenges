class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #greedy
        l = len(intervals)
        if(l==0):
            return 0
        if(l==1):
            return 0
        intervals.sort()
        prevItem=[]
        count=0
        for i,currItem in enumerate(intervals):
            #case1 [a,b] and [c,d], accept item2
            if(len(prevItem)==0 or prevItem[1]<=currItem[0]):
                # print("prev={},accept item {}".format(prevItem,currItem))
                count+=1
                prevItem=currItem
                
            #case2 [a [c,d] b], replace item1 with item2
            elif(prevItem[1]>currItem[0]) and (prevItem[1]>currItem[1]):
                # print("prev={},replace with item {}".format(prevItem,currItem))
                prevItem=currItem
                
            #case3 [a,{c,b]d}, reject item2
            # if(prevItem[1]>currItem[0]) and (prevItem[1]<currItem[1]):
            #     # print("prev={},reject item {}".format(prevItem,currItem))
            #     pass
              
        return l-count
            