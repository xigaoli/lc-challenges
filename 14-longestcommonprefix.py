class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        prefix=""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for item in strs:
                if(i>=len(item) or item[i]!=ch):
                    return prefix
            #all pass
            prefix+=ch
        return prefix
        