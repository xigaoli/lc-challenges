class Solution:
    def reorganizeString(self, S: str) -> str:
        #fill all the odd idx first, then fill the even idx
        sdict={}
        n=len(S)
        mostFreq=0
        mostFreqCh=0
        for ch in S:
            if(ch in sdict):
                sdict[ch]+=1
            else:
                sdict[ch]=1
            if(mostFreq<sdict[ch]):
                mostFreq=sdict[ch]
                mostFreqCh=ch

        if(mostFreq>(n+1)//2):
            return ""   #impossible
        rslt=[0]*n
        idx=0#even
        while(sdict[mostFreqCh]>0):
                rslt[idx]=mostFreqCh
                sdict[mostFreqCh]-=1
                idx+=2
                
        for ch in sdict.keys():
            while(sdict[ch]>0 and idx<n):
                rslt[idx]=ch
                sdict[ch]-=1
                idx+=2
            if(idx>=n): #outer loop
                break
                
        idx=1#odd
        for ch in sdict.keys():
            while(sdict[ch]>0 and idx<n):
                rslt[idx]=ch
                sdict[ch]-=1
                idx+=2
            if(idx>=n): #outer loop
                break
        #print(rslt)
        rsltstr = "".join(rslt)
        return rsltstr
            
            
            
        