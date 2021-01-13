class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #
        dp={}
        dp[0]=[""]
        dp[1]=["()"]
        
        def helper(k):
            #gen list of paren with k
            ans=[]
            if k in dp:
                return dp[k]
            
            for c in range(k):
                left=helper(c)
                right=helper(k-c-1)
                for item1 in left:
                    for item2 in right:
                        ans.append("({}){}".format(item1,item2))
            return ans
        ans = helper(n)
        return ans