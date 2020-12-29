class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        //imagine we already have a seq set (x1,x2,x3), if new set (Ai) can construct (x1Ai,x2Ai,x3Ai,[Ai-2,Ai-1,Ai]).
        //dp[i] is seq not in A[0..i-1] but in A[0...i], e.g. [1,3,4,5,6], dp[5]=num of ([3,4,5,6] and [4,5,6])==2, dp[4]=([3,4,5])==1
        //if(A[i]-A[i-1] == A[i-1]-A[i-2]) then dp[i]=dp[i-1]+1;else dp[i]=0
        int dp_prev=0;
        int rslt=0;
        for(int i=2;i<A.size();i++){
            if(A[i]-A[i-1]==A[i-1]-A[i-2])
            {
                //dp_prev+=1;
                rslt+=(++dp_prev);
            }
            else{
                dp_prev=0;
            }
        }
        return rslt;
        
    }
    
};
//optimization: we only use dp[i-1] to calc dp[i], so just use one var as dp_prev.