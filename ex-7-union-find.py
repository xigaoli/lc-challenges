class unionFindSet:
    #standard union-find data structure
    def __init__(self,size):
        self.parents = [i for i in range(size)] #initially parent[i] = i(self)
        self.sizes=[0]*size
        return
    def getSize(self,u):#get size of any set
        #find parent, parent rank is the size!
        return self.sizes[self.find(u)]
    def getSetCount(self):#return number of sets
        count=0
        for i in range(len(self.parents)):
            if(i==self.parents[i]):#root: parent == self
                count+=1
        return count
    def find(self,u):#find the root of set u
        if(u!=self.parents[u]):
            self.parents[u]=self.find(self.parents[u])
        return self.parents[u]
    def union(self,u,v):#join u and v
        pu = self.find(u)
        pv = self.find(v)
        if(pu==pv):
            #no need to join, same parent
            return False
        
        #join by rank
        #rank can mean number of elements
        #rank just made search parent less time
        if self.sizes[pu] > self.sizes[pv]:
            self.parents[pv] = pu
            self.sizes[pu] += self.sizes[pv]
        else:
            self.parents[pu]=pv
            self.sizes[pv]+=self.sizes[pu]
        return True