class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #store larger half of numbers
        self.minh=[]
        #store smaller half of numbers
        self.maxh=[]    #max heap store the negative value of elem
        
    def balance(self)->None:
        #remove top from minh
        elem1 = heapq.heappop(self.minh)
        #add to maxh
        heapq.heappush(self.maxh,elem1*-1)
        #adjust size
        if(len(self.minh)<len(self.maxh)):  #minh=[a,b],maxh=[c,d,e]
            elem1 = heapq.heappop(self.maxh)*-1
            heapq.heappush(self.minh,elem1)
        
        
    def addNum(self, num: int) -> None:
        #len of self.minh == self.maxh or len of self.minh-1 == self.maxh
        heapq.heappush(self.minh,num)
        self.balance()
            
        

    def findMedian(self) -> float:
        rslt=-1
        if(len(self.minh) == len(self.maxh)):
            #equal, peek 2 elements
            elem1=self.minh[0]
            elem2=self.maxh[0]*-1
            rslt= (elem1+elem2)/2.0
        else:
            #unequal, top of minh
            elem1 = self.minh[0]
            rslt= elem1
        #print("rslt={}".format(rslt))
        return rslt
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()