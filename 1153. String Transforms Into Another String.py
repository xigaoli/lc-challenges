class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        #guaranteed len(str1)==len(str2)
        #need one unused chars
        m1={}
        m2={}
        if(str1==str2):
            return True
        for i in range(len(str1)):
            ch1=str1[i]
            ch2=str2[i]
            
            if(ch1 not in m1):  #need ch1->ch2
                m1[ch1]=ch2
            elif(m1[ch1]!=ch2):
                return False    #one char cannot transform to 2 chars
        #if we want a->b,b->c,c->a, we need at least 1 tmp char to swap
        #if we want a->b,b->c, we need less than 26 chars in map(prevent loop)
        if(len(set(str2))>=26):
           return False
        return True