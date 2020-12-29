class Solution:
    #Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
    #Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
    #
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        outTotal=[]
        searchList=products
        for i in range(len(searchWord)):
            #currWord=searchWord[:i+1]
            currChar=searchWord[i]
            #print(currChar)
            count=0
            out=[]
            nextsearchList=[]
            for item in searchList:
                if(i<len(item) and item[i]==currChar):
                    nextsearchList.append(item)
                    if(count<3):
                        out.append(item)
                        count+=1
            #shorten the search list next time
            searchList = nextsearchList
            outTotal.append(out)
        return outTotal