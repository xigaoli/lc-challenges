from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        worddict = defaultdict(int)
        totalwcount = len(words)
        wlen = len(words[0])
        for item in words:
            worddict[item]+=1
        
        for i in range(len(s)):#check s[i:...] is a concat
            count = 0
            subdict = defaultdict(int)
            
            for j in range(totalwcount):
                wd = s[i+wlen*(j):i+wlen*(j+1)]
                if(subdict[wd]+1>worddict[wd]):#no match
                    break
                subdict[wd]+=1
                
                count+=1
                #print(wd)
            if(count == totalwcount):
                #print("found at index {}".format(i))
                ret.append(i)
        return ret
        