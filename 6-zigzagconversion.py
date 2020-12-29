class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        numOfRows=min(len(s),numRows)
        outlist =[""]*numOfRows
        direction=False
        currentRow=0
        for c in s:
            outlist[currentRow]+=c
            #print(outlist[currentRow])
            if(currentRow==numOfRows-1 or currentRow==0):
                direction= not direction
            if(direction==True):
                currentRow+=1
            else:
                currentRow-=1
        out="".join(outlist)
        return out