class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        inblock=False
        ans=[]
        newline=""
        for row in source:
            i=0
            if(inblock == False):
                newline=""
            while(i<len(row)):
                if(row[i:i+2]=="/*" and inblock==False):
                    inblock=True
                    i+=2
                elif(row[i:i+2]=="*/" and inblock==True):
                    inblock=False#end block
                    i+=2
                elif(row[i:i+2]=="//" and inblock==False):
                    break#end processing this line
                elif(inblock == False):
                    newline+=row[i]
                    i+=1
                else:#in a block
                    i+=1
            #print(newline)
            if(len(newline)>0 and inblock==False):
                ans.append(newline)
            
        return ans