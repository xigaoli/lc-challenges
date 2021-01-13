class WordFilter:

    def __init__(self, words: List[str]):
        self.pre={}
        self.suf={}
        for i in range(len(words)):
            word=words[i]
            for j in range(len(word)):
                item = word[:j+1]#prefix
                if(item not in self.pre):
                    self.pre[item]={}
                self.pre[item][word]=i
                
                item = word[j:]#suffix
                if(item not in self.suf):
                    self.suf[item]={}
                self.suf[item][word]=i
                
        
    def f(self, prefix: str, suffix: str) -> int:
        s1=set()
        s2=set()
        if(prefix in self.pre):
            d1=self.pre[prefix]
            for k in d1:
                s1.add(d1[k])
        if(suffix in self.suf):
            d2=self.suf[suffix]
            for k in d2:
                s2.add(d2[k])
        rslt = s1.intersection(s2)
        if(len(rslt)==0):
            return -1
        rslt = max(rslt)
        return rslt
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)