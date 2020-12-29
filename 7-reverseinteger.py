class Solution:
    def reverse(self, x: int) -> int:
        if(x==0):
            return 0
        iFlag=1
        if(x<0):
            iFlag=-1
        x=x*iFlag
        digit=0
        a=x
        count=0
        while a!=0:
            count+=1
            a=a//10
        r=0
        for i in range(count):
            digit=x%10
            x=x//10
            r+=digit*10**(count-i-1)
        r*=iFlag
        if(r<(-1*2**31) or r>(2**31-1)):
            return 0
        return r
            