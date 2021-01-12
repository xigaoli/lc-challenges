class Bnode:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.left=None
        self.right=None
    def insert(self,event):#event is a node
        #insert a node,either event.end<-self.begin, or self.end->event.begin, or false
        #return false for ins fail
        if(event.end<=self.start):
            #event->...->self->...
            if(self.left is None):
                self.left = event
                return True
            else:
                rslt = self.left.insert(event)#insert into left recursively
                return rslt
        elif(self.end<=event.start):
            #self->...->event->...
            if(self.right is None):
                self.right=event
                return True
            else:
                rslt = self.right.insert(event)#insert into left recursively
                return rslt
        else:
            #cannot insert, have overlap
            return False
        

class MyCalendar:

    def __init__(self):
        self.tb = None
        

    def book(self, start: int, end: int) -> bool:
        #overlapping integer
        #sort by start, find a<start, find b>end, so we have [a,start,end,b]
        #check all stuff in [a,b], see if overlap
        if(self.tb is None):
            self.tb = Bnode(start,end)
            return True
        else:
            eventitem = Bnode(start,end)
            
            rslt = self.tb.insert(eventitem)
            return rslt
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)