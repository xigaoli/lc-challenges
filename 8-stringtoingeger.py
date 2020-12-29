class Solution:
    def myAtoi(self, str: str) -> int:
        digitDict={"0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9 }
        started=False
        pFlag=1
        digitlist=[]
        for i in range(len(str)):
            if(str[i]!=' ' and started == False):
                started=True
                if(str[i]=="+"):
                    pFlag=1
                    continue
                elif(str[i]=="-"):
                    pFlag=-1
                    continue
                elif(str[i] in digitDict.keys()):
                    pass
                else:
                    #parse fail
                    return 0
            if(started==True):
                #start counting chars
                if(str[i] in digitDict.keys()):
                    digitlist.append(digitDict[str[i]])
                else:
                    #stop here
                    break
        l = len(digitlist)-1
        s=0
        for d in digitlist:
            s+=d*(10**l)
            l-=1
        s=s*pFlag
        if(s>(2**31-1)):
            return (2**31-1)
        if(s<(-1*(2**31))):
            return (-1*(2**31))
        return s