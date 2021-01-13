class Node:
    def __init__(self,val,freq):
        self.freq=freq
        self.val=val
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minfreq=1
        self.freq = {} #key:int, value:orderedDict(int), 
        #storing key in this self.freq[freq] by FIFO order, head of orderedDict will be least frequent used (list(self.freq[freq]).firstelement), 
        
        self.cache = {} #key:int, value:Node
        
    def updateKeyFreq(self,item,key)->None:
        #key freq +=1
        
        
        freqlist = self.freq[item.freq]
        freqlist = self.freq[item.freq]#orderedDict
        del freqlist[key] #must be in here
        if(len(freqlist)==0):
            del self.freq[item.freq]#release mem?
            
        item.freq+=1
        if(item.freq not in self.freq):
            self.freq[item.freq]=OrderedDict()
        self.freq[item.freq][key]=1
        
        
        return
    def get(self, key: int) -> int:
        #print("get:key={}".format(key))
        if(key in self.cache):
            item = self.cache[key]
            self.updateKeyFreq(item,key)
            
            return item.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(self.capacity==0):
            return
        #print("put:key={}".format(key))
        if(key in self.cache):
            item = self.cache[key]
            item.val = value
            self.updateKeyFreq(item,key)
            
            #print("put old:key={}".format(key))
            
        else:
            self.purge()
            item = Node(value,1)#new item freq 1
            self.cache[key]=item
            #print("put new:key={}".format(key))
            
            #new key added into self.freq
            if(item.freq not in self.freq):
                self.freq[item.freq]=OrderedDict()
            self.freq[item.freq][key]=1
            
            
        return
    def purge(self):
        if(len(self.cache)+1<=self.capacity):
            #fine...
            return
        #make capacity -=1
        print(self.freq.keys())
        minfreq = min(self.freq.keys())
        #purge the oldest
        freqlist = self.freq[minfreq]#orderedDict
        #remove the first item
        #print("minfreq={},freqlist={}".format(minfreq,freqlist.keys()))
        oldestkey=next(iter(freqlist))#the front item
        #print("del key={}".format(oldestkey))
        del freqlist[oldestkey]
        del self.cache[oldestkey]
        if(len(freqlist)==0):
            
            del self.freq[minfreq]#release mem?
            #print("deleted minfreq={}, self.freq={}".format(minfreq,self.freq.keys()))
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)