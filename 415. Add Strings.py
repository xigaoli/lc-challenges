class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        p1=len(num1)-1
        p2=len(num2)-1
        base=0
        CF=0
        sum1=0
        while p1>=0 or p2>=0:
            if(p1<0):
                s1=0
            else:
                s1=int(num1[p1])
            if(p2<0):
                s2=0
            else:
                s2=int(num2[p2])
            s=s1+s2
            sum1+=(s+CF)*(10**base)
            base+=1
            p1-=1
            p2-=1
        return str(sum1)
            