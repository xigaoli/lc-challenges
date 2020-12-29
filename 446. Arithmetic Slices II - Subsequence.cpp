class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        //similar to arithmetic slice 1
        //we only count it to ans if it gets +1'ed; in other words, if +1 successful, we count previous sequence into ans.
        int n = A.size();
        long long ans=0;
        unordered_map<long long,int>* dp = new unordered_map<long long,int>[n];
        unordered_set<int> arrset = unordered_set<int>(A.begin(),A.end());      //optimization for map storage
        
        //vector<unordered_map<long long,int>> dp(n);
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                //calc dp[i][d]
                long long d=(long long)A[i]-(long long)A[j];
                int t= 0;
                if(dp[j].find(d)!=dp[j].end()){
                    t=dp[j][d];
                }
                if(arrset.count(A[i]+d)>0){
                    // if A[i]+d does not exist, we do not need it ever after, e.g. [1,100,2,3], we never use diff=50 later
                    dp[i][d]+=t+1;
                }
                ans+=t;//important: if and only if it gets +1'ed, means this can be added into true answer
            }
            
        }
        delete[] dp;
        return (int)ans;
    }
};