class unionFindSet:
    #standard union-find data structure
    def __init__(self,size):
        self.parents = [i for i in range(size)] #initially parent[i] = i(self)
        self.rank=[0]*size
        return
    def getSize(self,u):#get size of any set
        #find parent, parent rank is the size!
        return self.rank[self.find(u)]
    
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
        if self.rank[pu] > self.rank[pv]:
            self.parents[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parents[pu]=pv
            self.rank[pv]+=self.rank[pu]
        return True
        
    
class Solution:
    
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if(m==len(arr)):#only at step m, we will have a group of len m
            return m
        #init new uf set
        uf = unionFindSet(len(arr))
        #bits=[0]*len(arr)  #help to visualize
        ans = -1
        for step in range(len(arr)):
            bitidx = arr[step]-1
            #set bitidx as 1 (new set with rank 1)
            #bits[bitidx]=1
            #print(bits)
            
            uf.rank[bitidx]=1
            #check left
            if(bitidx-1>=0 and uf.rank[bitidx-1] >0):#something in the left
                
                if(uf.getSize(bitidx-1) == m):
                    #before merge, have size m: must trace to root to see actual size!
                    ans=step
                uf.union(bitidx-1,bitidx) #merge two groups [left mid]
            #check right
            if(bitidx+1<len(arr) and uf.rank[bitidx+1]>0):#something in the right
                
                if(uf.getSize(bitidx+1) == m):
                    #before merge, have size m: must trace to root to see actual size!
                    ans=step
                uf.union(bitidx+1,bitidx) #merge two groups [mid right]
                
            
        return ans
                
            
        